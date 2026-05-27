# Observability

## Structured Logging
- **Framework**: `structlog` (Python library).
- **Format**: Output in clean Console Format in development (or if `APP_DEBUG=true`), and JSON format in production.
- **Correlation**: Request ID (`X-Request-ID`) tracking across the lifespan of a web request. Request IDs are injected by a FastAPI middleware and propagated in logs and responses.

## Metrics
- **Prometheus**: Setup via `prometheus-fastapi-instrumentator`.
- **Exposed endpoint**: `GET /api/metrics`.
- **Key Metrics Tracked**:
  - HTTP requests count (by code, route, method).
  - Database pool size and queue depth.
  - LLM API call latency and failure rates.

## Error Tracking
- Uncaught exceptions are intercepted by a global exception handler, logged with stack traces, and returned to client as generic `500 Internal Server Error` to prevent exposing internals.
