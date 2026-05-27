import uuid
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import verify_token
from app.core.exceptions import InvalidTokenException
from app.models.user import User
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)
user_repository = UserRepository()

async def get_current_user(
    token: str | None = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    if not token:
        raise InvalidTokenException("Not authenticated. Bearer token missing.")

    payload = verify_token(token)
    user_id_str = payload.get("sub")
    if not user_id_str:
        raise InvalidTokenException("Invalid token payload. Subject missing.")

    try:
        user_id = uuid.UUID(user_id_str)
    except ValueError as e:
        raise InvalidTokenException("Invalid token payload. Subject format error.") from e

    user = await user_repository.get_by_id(db, user_id)
    if not user:
        raise InvalidTokenException("User not found.")
    
    if not user.is_active:
        raise InvalidTokenException("User account is inactive.")

    return user
