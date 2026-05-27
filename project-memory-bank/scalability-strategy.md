# Scalability Strategy

## Architecture Scalability
- **Stateless Applications**: Both Next.js frontend and FastAPI backend are entirely stateless. They can scale horizontally by launching additional instances behind a load balancer (e.g. Google Cloud Run).
- **Session Decoupling**: NextAuth.js uses standard JWT session tokens, meaning the Next.js server does not maintain sticky state. FastAPI relies on database-backed and self-verifiable bearer JWT tokens.

## Cache Layer
- **Redis 7**: Used to store user permissions, rate-limiting counters, and responses that undergo frequent reads but rare writes.
- **Connection Pooling**: Re-uses DB and Redis connections to prevent exhaustion during traffic spikes.

## Vector Query Performance
- ChromaDB runs locally in early development. For production (Phase 8), it will be migrated to a dedicated service like Pinecone or pgvector indexes within Google Cloud SQL.
