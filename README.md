# AI-Native Student Execution OS

An autonomous, persistent AI operating system that transforms student intent into measurable achievement through specialized execution agents.

## Architectural Overview

The system uses a decoupled experience-and-resource design:
- **Frontend**: Next.js 15 (App Router, Tailwind CSS v4, Auth.js v5). Handles UI representation and edge authentication.
- **Backend**: FastAPI (Python 3.12, asyncpg, SQLAlchemy 2.0, structlog). Serves REST API resources, manages database entities, and coordinates LLM agents.
- **Database**: PostgreSQL 16 relational data store.
- **Cache & Tasks**: Redis 7 active cache and asynchronous tasks scheduler.

---

## Local Development Setup

To run the full stack locally with hot-reload support, use Docker Compose:

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Node.js v20+ (for local frontend scripting)
- Python 3.12+ (for local backend development)

### Booting the Stack
1. Clone the repository.
2. Initialize environment files:
   - Copy `backend/.env.example` to `backend/.env`
   - Copy `frontend/.env.example` to `frontend/.env.local`
3. Spin up the container services:
   ```bash
   docker compose -f infrastructure/docker/docker-compose.yml up --build
   ```
4. Access the applications:
   - **Frontend UI**: [http://localhost:3000](http://localhost:3000)
   - **Backend API Docs (Swagger)**: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
   - **Backend Health Check**: [http://localhost:8000/api/health/ready](http://localhost:8000/api/health/ready)

---

## Project Structure

```text
AI-Native-Student-Execution-OS-Reloaded/
├── project-memory-bank/       # AI persistent coordination layer (20 files)
├── frontend/                  # Next.js 15 app
│   ├── src/
│   │   ├── app/               # App Router pages and layouts
│   │   ├── components/        # Shared components
│   │   ├── lib/               # Utility API client, NextAuth setup
│   │   └── types/             # Custom typescript definitions
├── backend/                   # FastAPI app
│   ├── app/
│   │   ├── api/               # Router endpoints and Pydantic schemas
│   │   ├── core/              # Database, middleware, security, and logging config
│   │   ├── models/            # SQLAlchemy database models
│   │   └── services/          # Core auth and operational services
│   ├── alembic/               # Database migrations folder
└── infrastructure/            # Docker configs and scripts
    └── docker/
        └── docker-compose.yml
```

---

## Email Verification Fallback

For local development, email sending is printed directly to the backend server logs. Simply open the logs, locate the generated verification link, and paste it into your browser to verify accounts created with Email/Password. To enable actual email deliveries, configure `APP_RESEND_API_KEY` in `backend/.env`.
