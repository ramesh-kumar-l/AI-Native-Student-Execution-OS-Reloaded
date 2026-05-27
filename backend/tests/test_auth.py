import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, VerificationToken

@pytest.mark.asyncio
async def test_user_registration_success(client: AsyncClient, db_session: AsyncSession):
    register_payload = {
        "email": "test@example.com",
        "password": "secure_password_123",
        "full_name": "Test Student"
    }
    response = await client.post("/api/v1/auth/register", json=register_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test Student"
    assert data["email_verified"] is False
    assert "Verification email sent" in data["message"]

    # Verify user is saved in DB
    result = await db_session.execute(select(User).where(User.email == "test@example.com"))
    user = result.scalars().first()
    assert user is not None
    assert user.full_name == "Test Student"

    # Verify verification token is created
    tok_result = await db_session.execute(select(VerificationToken).where(VerificationToken.user_id == user.id))
    token = tok_result.scalars().first()
    assert token is not None
    assert len(token.token) > 0

@pytest.mark.asyncio
async def test_email_verification_flow(client: AsyncClient, db_session: AsyncSession):
    # 1. Register
    register_payload = {
        "email": "verify@example.com",
        "password": "secure_password_123",
        "full_name": "Verify Student"
    }
    await client.post("/api/v1/auth/register", json=register_payload)

    # Fetch token from DB
    result = await db_session.execute(select(User).where(User.email == "verify@example.com"))
    user = result.scalars().first()
    tok_result = await db_session.execute(select(VerificationToken).where(VerificationToken.user_id == user.id))
    token = tok_result.scalars().first()

    # 2. Verify Email
    verify_response = await client.get(f"/api/v1/auth/verify-email?token={token.token}")
    assert verify_response.status_code == 200
    assert "Email successfully verified" in verify_response.json()["message"]

    # Re-fetch user and verify email_verified flag is true
    await db_session.refresh(user)
    assert user.email_verified is True

@pytest.mark.asyncio
async def test_login_and_access_protected_route(client: AsyncClient, db_session: AsyncSession):
    # 1. Register & verify user email
    register_payload = {
        "email": "login@example.com",
        "password": "secure_password_123",
        "full_name": "Login Student"
    }
    await client.post("/api/v1/auth/register", json=register_payload)
    
    result = await db_session.execute(select(User).where(User.email == "login@example.com"))
    user = result.scalars().first()
    user.email_verified = True
    await db_session.commit()

    # 2. Login
    login_payload = {
        "email": "login@example.com",
        "password": "secure_password_123"
    }
    login_response = await client.post("/api/v1/auth/login", json=login_payload)
    assert login_response.status_code == 200
    tokens = login_response.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens
    assert tokens["token_type"] == "bearer"

    # 3. Access Protected Route /me
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    me_response = await client.get("/api/v1/auth/me", headers=headers)
    assert me_response.status_code == 200
    profile = me_response.json()
    assert profile["email"] == "login@example.com"
    assert profile["full_name"] == "Login Student"
    assert profile["email_verified"] is True
