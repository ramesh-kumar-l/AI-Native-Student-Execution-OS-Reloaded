import asyncio
from typing import AsyncGenerator
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.main import app
from app.core.database import get_db, Base

# Use in-memory SQLite database for fast isolated unit tests
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()

@pytest.fixture(autouse=True)
async def override_db(db_session: AsyncSession):
    # Override FastAPI get_db dependency
    app.dependency_overrides[get_db] = lambda: db_session
    yield
    app.dependency_overrides.clear()

@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    # Use ASGITransport to communicate directly with app without starting real network sockets
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
