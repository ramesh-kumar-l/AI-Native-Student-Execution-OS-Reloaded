from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.schemas.auth import (
    UserRegister, UserLogin, GoogleLogin, TokenRefresh,
    TokenResponse, UserResponse, RegisterResponse
)
from app.services.auth_service import AuthService
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])
auth_service = AuthService()

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(
    register_data: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    return await auth_service.register(db, register_data)

@router.get("/verify-email", status_code=status.HTTP_200_OK)
async def verify_email(
    token: str,
    db: AsyncSession = Depends(get_db)
):
    await auth_service.verify_email(db, token)
    return {"status": "verified", "message": "Email successfully verified. You can now log in."}

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(
    login_data: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    return await auth_service.login(db, login_data)

@router.post("/google", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def google_login(
    google_data: GoogleLogin,
    db: AsyncSession = Depends(get_db)
):
    return await auth_service.google_login(db, google_data)

@router.post("/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def refresh(
    refresh_data: TokenRefresh,
    db: AsyncSession = Depends(get_db)
):
    return await auth_service.refresh_tokens(db, refresh_data.refresh_token)

@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user
