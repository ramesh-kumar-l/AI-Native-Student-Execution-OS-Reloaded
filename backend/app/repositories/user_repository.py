import uuid
from datetime import datetime, timezone
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, VerificationToken, RefreshToken

class UserRepository:
    async def get_by_id(self, db: AsyncSession, user_id: uuid.UUID) -> User | None:
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def get_by_google_id(self, db: AsyncSession, google_id: str) -> User | None:
        result = await db.execute(select(User).where(User.google_id == google_id))
        return result.scalars().first()

    async def create(self, db: AsyncSession, user: User) -> User:
        db.add(user)
        await db.flush()
        return user

    async def update_last_login(self, db: AsyncSession, user_id: uuid.UUID) -> None:
        await db.execute(
            update(User)
            .where(User.id == user_id)
            .values(last_login_at=datetime.now(timezone.utc))
        )

    # Verification token operations
    async def create_verification_token(self, db: AsyncSession, token: VerificationToken) -> VerificationToken:
        db.add(token)
        await db.flush()
        return token

    async def get_verification_token(self, db: AsyncSession, token_str: str) -> VerificationToken | None:
        result = await db.execute(select(VerificationToken).where(VerificationToken.token == token_str))
        return result.scalars().first()

    async def delete_verification_token(self, db: AsyncSession, token_id: uuid.UUID) -> None:
        token = await db.get(VerificationToken, token_id)
        if token:
            await db.delete(token)

    # Refresh token operations
    async def create_refresh_token(self, db: AsyncSession, refresh_token: RefreshToken) -> RefreshToken:
        db.add(refresh_token)
        await db.flush()
        return refresh_token

    async def get_refresh_token(self, db: AsyncSession, token_str: str) -> RefreshToken | None:
        result = await db.execute(select(RefreshToken).where(RefreshToken.token == token_str))
        return result.scalars().first()

    async def revoke_refresh_tokens(self, db: AsyncSession, user_id: uuid.UUID) -> None:
        await db.execute(
            update(RefreshToken)
            .where(RefreshToken.user_id == user_id)
            .values(is_revoked=True)
        )
