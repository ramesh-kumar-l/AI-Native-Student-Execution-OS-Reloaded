from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App General Settings
    APP_NAME: str = "AI-Native Student Execution OS"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # Security
    # In production, this must be a strong 32-character string. SecretStr masks this value.
    SECRET_KEY: SecretStr = SecretStr("change-this-to-a-very-secure-secret-key-32-chars-at-least-!")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Database URLs
    # Format: postgresql+asyncpg://user:pass@host:5432/db
    DATABASE_URL: SecretStr = SecretStr("postgresql+asyncpg://postgres:postgres@db:5432/ai_student_os")

    # Redis Cache URL
    REDIS_URL: str = "redis://redis:6379/0"

    # Google Credentials (for verification/OAuth)
    GOOGLE_CLIENT_ID: str = ""

    # Resend API Key for sending emails
    RESEND_API_KEY: SecretStr = SecretStr("")
    FROM_EMAIL: str = "onboarding@resend.dev"

    # CORS Allowed Origins
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        case_sensitive=True,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
