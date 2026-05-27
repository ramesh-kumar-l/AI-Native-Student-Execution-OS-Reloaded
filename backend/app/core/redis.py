from redis.asyncio import Redis, ConnectionPool
from app.core.config import get_settings

settings = get_settings()

# Initialize connection pool for Redis
redis_pool = ConnectionPool.from_url(
    settings.REDIS_URL,
    max_connections=20,
    decode_responses=True
)

async def get_redis() -> Redis:
    return Redis(connection_pool=redis_pool)
