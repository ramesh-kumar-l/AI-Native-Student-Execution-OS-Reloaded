from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from app.core.config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL.get_secret_value(),
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,  # Set to True to log raw SQL queries
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # CRITICAL for async to avoid lazy load errors
)

class Base(AsyncAttrs, DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
