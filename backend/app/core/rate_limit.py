import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from app.core.config import get_settings

settings = get_settings()

async def init_rate_limiter():
    """
    Initializes the Redis connection for FastAPI Limiter.
    """
    redis_conn = redis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
    await FastAPILimiter.init(redis_conn)

async def close_rate_limiter():
    """
    Closes the Redis connection for FastAPI Limiter.
    """
    await FastAPILimiter.close()
