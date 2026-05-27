import json
import structlog
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

from app.core.database import get_db
from app.core.redis import get_redis

logger = structlog.get_logger()
router = APIRouter(tags=["Health"])

@router.get("/health/live", status_code=status.HTTP_200_OK)
async def liveness():
    """Liveness probe. No dependencies checked, just that HTTP server is responsive."""
    return {"status": "alive"}

@router.get("/health/ready")
async def readiness(
    db: AsyncSession = Depends(get_db),
    redis: Redis = Depends(get_redis)
):
    """Readiness probe. Checks status of PostgreSQL and Redis connections."""
    checks = {}

    # Check Database connection
    try:
        await db.execute(text("SELECT 1"))
        checks["database"] = "healthy"
    except Exception as e:
        logger.error("database_health_check_failed", error=str(e))
        checks["database"] = f"unhealthy: {str(e)}"

    # Check Redis connection
    try:
        await redis.ping()
        checks["redis"] = "healthy"
    except Exception as e:
        logger.error("redis_health_check_failed", error=str(e))
        checks["redis"] = f"unhealthy: {str(e)}"

    all_healthy = all(v == "healthy" for v in checks.values())
    status_code = status.HTTP_200_OK if all_healthy else status.HTTP_503_SERVICE_UNAVAILABLE

    return Response(
        content=json.dumps({
            "status": "ready" if all_healthy else "degraded",
            "checks": checks
        }),
        status_code=status_code,
        media_type="application/json"
    )
