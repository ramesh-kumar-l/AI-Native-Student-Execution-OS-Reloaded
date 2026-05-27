from datetime import datetime, timedelta, timezone
from typing import Any
import jwt
from pwdlib import PasswordHash

from app.core.config import get_settings

settings = get_settings()
password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return password_hash.verify(password, hashed)

def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({
        "exp": expire,
        "iss": settings.APP_NAME,
        "aud": settings.APP_NAME,
        "type": "access"
    })
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY.get_secret_value(),
        algorithm="HS256"
    )

def create_refresh_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    to_encode.update({
        "exp": expire,
        "iss": settings.APP_NAME,
        "aud": settings.APP_NAME,
        "type": "refresh"
    })
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY.get_secret_value(),
        algorithm="HS256"
    )

def verify_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY.get_secret_value(),
            algorithms=["HS256"],
            audience=settings.APP_NAME,
            issuer=settings.APP_NAME
        )
    except jwt.ExpiredSignatureError as e:
        from app.core.exceptions import TokenExpiredException
        raise TokenExpiredException() from e
    except jwt.PyJWTError as e:
        from app.core.exceptions import InvalidTokenException
        raise InvalidTokenException() from e
