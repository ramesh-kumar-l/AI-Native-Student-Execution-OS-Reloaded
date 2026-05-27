from contextlib import asynccontextmanager
from fastapi import FastAPI
import structlog

from app.core.config import get_settings
from app.core.database import engine
from app.core.redis import redis_pool
from app.core.logging import setup_logging
from app.core.middleware import setup_cors, CorrelationIdMiddleware
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router

settings = get_settings()
logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup structured logging according to environment setting
    setup_logging(
        json_logs=(settings.ENVIRONMENT != "development"),
        log_level=settings.LOG_LEVEL
    )
    logger.info("application_starting", environment=settings.ENVIRONMENT, version="0.1.0")
    
    yield
    
    logger.info("application_shutting_down")
    # Clean up connections
    await redis_pool.disconnect()
    await engine.dispose()

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
)

# Setup Middlewares (CORS first)
setup_cors(app)
app.add_middleware(CorrelationIdMiddleware)

# Expose HTTP endpoint routers
app.include_router(health_router, prefix="/api")
app.include_router(auth_router, prefix="/api/v1")
