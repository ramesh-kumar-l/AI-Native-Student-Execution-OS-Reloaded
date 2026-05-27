import uuid
import secrets
from datetime import datetime, timedelta, timezone
import structlog
import resend
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token
from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    EmailNotVerifiedException,
    InvalidTokenException
)
from app.models.user import User, VerificationToken, RefreshToken
from app.repositories.user_repository import UserRepository
from app.api.schemas.auth import UserRegister, UserLogin, GoogleLogin, TokenResponse, RegisterResponse

logger = structlog.get_logger()
settings = get_settings()
user_repository = UserRepository()

class AuthService:
    def __init__(self):
        # Configure Resend client
        resend_key = settings.RESEND_API_KEY.get_secret_value()
        if resend_key:
            resend.api_key = resend_key

    async def register(self, db: AsyncSession, register_data: UserRegister) -> RegisterResponse:
        # Check if user already exists
        existing_user = await user_repository.get_by_email(db, register_data.email)
        if existing_user:
            logger.warn("registration_failed_email_taken", email=register_data.email)
            raise UserAlreadyExistsException()

        # Create user
        hashed = hash_password(register_data.password)
        new_user = User(
            email=register_data.email,
            password_hash=hashed,
            full_name=register_data.full_name,
            auth_provider="credentials",
            email_verified=False,
            is_active=True
        )
        
        user = await user_repository.create(db, new_user)
        
        # Generate verification token
        token_str = secrets.token_urlsafe(32)
        expires_at = datetime.now(timezone.utc) + timedelta(hours=24)
        verification_token = VerificationToken(
            user_id=user.id,
            token=token_str,
            token_type="email_verification",
            expires_at=expires_at
        )
        
        await user_repository.create_verification_token(db, verification_token)
        
        # Trigger Email
        await self._send_verification_email(user.email, user.full_name, token_str)
        
        return RegisterResponse(
            id=user.id,
            email=user.email,
            full_name=user.full_name,
            email_verified=user.email_verified,
            message="Verification email sent."
        )

    async def verify_email(self, db: AsyncSession, token_str: str) -> None:
        db_token = await user_repository.get_verification_token(db, token_str)
        if not db_token:
            logger.warn("email_verification_failed_token_not_found", token=token_str)
            raise InvalidTokenException("Verification token is invalid or has expired.")

        if db_token.expires_at < datetime.now(timezone.utc):
            logger.warn("email_verification_failed_token_expired", token=token_str)
            await user_repository.delete_verification_token(db, db_token.id)
            raise InvalidTokenException("Verification token is invalid or has expired.")

        # Load user
        user = await user_repository.get_by_id(db, db_token.user_id)
        if not user:
            raise InvalidTokenException("User not found.")

        # Activate user
        user.email_verified = True
        
        # Delete token
        await user_repository.delete_verification_token(db, db_token.id)
        logger.info("email_verified_successfully", user_id=user.id, email=user.email)

    async def login(self, db: AsyncSession, login_data: UserLogin) -> TokenResponse:
        user = await user_repository.get_by_email(db, login_data.email)
        if not user:
            logger.warn("login_failed_user_not_found", email=login_data.email)
            raise InvalidCredentialsException()

        if user.auth_provider != "credentials" or not user.password_hash:
            logger.warn("login_failed_wrong_auth_provider", email=login_data.email, provider=user.auth_provider)
            raise InvalidCredentialsException()

        if not verify_password(login_data.password, user.password_hash):
            logger.warn("login_failed_wrong_password", email=login_data.email)
            raise InvalidCredentialsException()

        if not user.email_verified:
            logger.warn("login_failed_email_not_verified", email=login_data.email)
            raise EmailNotVerifiedException()

        return await self._create_user_tokens(db, user)

    async def google_login(self, db: AsyncSession, google_data: GoogleLogin) -> TokenResponse:
        # In a real environment, we would verify the id_token using google-auth library
        # e.g.: idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        # For Phase 1 foundational bootstrap, we will parse details or stub the verification.
        # Let's extract stub details (e.g. from a JWT-like format or provide a mock email/name)
        # To make it testable, we allow a mock payload or direct claims mapping.
        # For now, let's treat the token as email if it looks like one, or parse claims.
        # If it doesn't verify, in local dev we will stub it.
        email = f"google-{google_data.id_token[:8]}@example.com"
        full_name = "Google User"
        google_id = f"g-{google_data.id_token}"

        # Try to find user by google_id
        user = await user_repository.get_by_google_id(db, google_id)
        if not user:
            # Check if user with same email exists
            user_by_email = await user_repository.get_by_email(db, email)
            if user_by_email:
                # Link account
                user_by_email.google_id = google_id
                user_by_email.auth_provider = "google"
                user_by_email.email_verified = True
                user = user_by_email
                logger.info("google_account_linked_to_existing_email", user_id=user.id)
            else:
                # Create new Google user
                new_user = User(
                    email=email,
                    full_name=full_name,
                    auth_provider="google",
                    google_id=google_id,
                    email_verified=True,
                    is_active=True
                )
                user = await user_repository.create(db, new_user)
                logger.info("google_user_registered", user_id=user.id, email=email)
        else:
            logger.info("google_user_logged_in", user_id=user.id)

        return await self._create_user_tokens(db, user)

    async def refresh_tokens(self, db: AsyncSession, refresh_token_str: str) -> TokenResponse:
        db_token = await user_repository.get_refresh_token(db, refresh_token_str)
        if not db_token or db_token.is_revoked or db_token.expires_at < datetime.now(timezone.utc):
            logger.warn("refresh_failed_invalid_or_expired_token")
            raise InvalidTokenException("Refresh token is invalid or has expired.")

        user = await user_repository.get_by_id(db, db_token.user_id)
        if not user:
            raise InvalidTokenException("User not found.")

        # Revoke old refresh tokens for safety
        await user_repository.revoke_refresh_tokens(db, user.id)

        # Create new tokens
        return await self._create_user_tokens(db, user)

    async def _create_user_tokens(self, db: AsyncSession, user: User) -> TokenResponse:
        user_data = {"sub": str(user.id), "email": user.email, "role": user.role}
        access_token = create_access_token(user_data)
        refresh_token_val = create_refresh_token(user_data)

        # Persist refresh token
        expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        db_refresh_token = RefreshToken(
            user_id=user.id,
            token=refresh_token_val,
            expires_at=expires_at
        )
        await user_repository.create_refresh_token(db, db_refresh_token)

        # Update last login
        await user_repository.update_last_login(db, user.id)

        logger.info("user_session_created", user_id=user.id)
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token_val,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )

    async def _send_verification_email(self, email: str, name: str, token: str):
        verification_url = f"http://localhost:3000/verify-email?token={token}"
        subject = "Verify your email - AI Student Execution OS"
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px;">
                <h2 style="color: #8b5cf6;">Welcome to AI Student Execution OS, {name}!</h2>
                <p>Thank you for signing up. Please verify your email by clicking the button below:</p>
                <div style="margin: 20px 0;">
                    <a href="{verification_url}" style="background-color: #6366f1; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; display: inline-block;">Verify Email Address</a>
                </div>
                <p style="font-size: 12px; color: #94a3b8;">If you did not sign up for this account, please ignore this email.</p>
                <p style="font-size: 12px; color: #94a3b8;">Or copy this link: {verification_url}</p>
            </body>
        </html>
        """

        resend_key = settings.RESEND_API_KEY.get_secret_value()
        if resend_key:
            try:
                resend.Emails.send({
                    "from": settings.FROM_EMAIL,
                    "to": email,
                    "subject": subject,
                    "html": html_content
                })
                logger.info("email_verification_sent_via_resend", email=email)
            except Exception as e:
                logger.error("email_sending_failed", error=str(e))
                # Fallback to logging for development resilience
                self._log_email_fallback(email, verification_url)
        else:
            self._log_email_fallback(email, verification_url)

    def _log_email_fallback(self, email: str, verification_url: str):
        logger.info(
            "email_verification_console_fallback",
            email=email,
            verification_url=verification_url,
            message="No Resend key configured. Please copy the verification link to proceed."
        )
