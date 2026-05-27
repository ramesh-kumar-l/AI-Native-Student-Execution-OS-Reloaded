# Architecture Summary

## System Context
The AI-Native Student Execution OS is built as a split-architecture application:
1. **Experience Layer (Frontend)**: Next.js 15 App Router. Serves the user interface, manages sessions via Auth.js, handles routing, and forwards requests to the API Layer.
2. **API Layer (Backend)**: FastAPI (Python). Manages business logic, coordinates AI execution agents, triggers background tasks, and performs database queries.
3. **Storage Layer**: PostgreSQL 16 for relational data (users, tasks, calendars) and Vector DB (ChromaDB) for document chunks and vector space queries.
4. **Cache & Task Queue**: Redis 7 for cache management and async background task scheduling (using ARQ).

```
[ User Browser ]
       │ (HTTPS / WebSockets)
       ▼
┌─────────────────────────┐
│       Next.js 15        │  (Experience Layer)
│    Frontend Server      │
└──────────┬──────────────┘
           │ (Internal API Calls / JWT Bearer)
           ▼
┌─────────────────────────┐
│     FastAPI Backend     │  (API Layer & Agents)
└────┬───────────────┬────┘
     │               │
     ▼ (SQL / Async) ▼ (Redis Protocol)
┌──────────┐   ┌───────────┐
│ Postgres │   │  Redis 7  │  (Data & Task State)
│    16    │   │  & ARQ    │
└──────────┘   └───────────┘
```

## Core Design Principles
- **Loose Coupling**: Bounded contexts (Auth, Students, Learning, AI) do not import each other's database schemas directly. They communicate via interfaces.
- **Async First**: All database queries, Redis connections, and HTTP clients (HTTPX) in the backend are fully asynchronous to prevent blocking.
- **Fail-Safe Security**: Backend verify-on-request JWT design. The database never exposes unhashed secrets.
