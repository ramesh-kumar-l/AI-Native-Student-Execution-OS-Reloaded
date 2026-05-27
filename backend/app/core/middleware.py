import os
import uuid
import structlog
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars

from app.core.config import get_settings

logger = structlog.get_logger()
settings = get_settings()

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Injects or gets the request transaction ID
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        bind_contextvars(
            request_id=request_id,
            method=request.method,
            path=request.url.path,
        )
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        clear_contextvars()
        return response

def setup_cors(app: FastAPI):
    allowed_origins = [
        origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",") if origin.strip()
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "X-Request-ID"],
        expose_headers=["X-Request-ID"],
        max_age=600,
    )
