# Deployment Notes

## Local Environment Setup
We use Docker Compose for local execution of the application components.

### Requirements
- Docker and Docker Compose installed.
- Node.js (v20+ recommended) for local package running.
- Python 3.12+ (for backend development outside of containers).

### Initializing Stack
```bash
docker compose -f infrastructure/docker/docker-compose.yml up --build
```
This starts PostgreSQL, Redis, Backend (FastAPI), and Frontend (Next.js 15).

## Production Target
Planned for Google Cloud Run (Phase 8).
- Multi-stage Docker builds.
- Database: Cloud SQL (PostgreSQL).
- Caching: Cloud Memorystore (Redis).
