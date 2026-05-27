# Decisions

## ADR 1: Monorepo vs Polyrepo
- **Decision**: Monorepo.
- **Rationale**: Keeps frontend, backend, packages, and infra configurations in a single version-controlled repository. Easier to manage types, contracts, and Docker setups for small to medium-sized teams.
- **Trade-offs**: Build caching and CI triggers must be scoped to subdirectories to avoid full rebuilds on minor changes.

## ADR 2: Tech Stack selection
- **Decision**: Next.js 15 (App Router, TS, Tailwind) + FastAPI (Python 3.12+, async SQLAlchemy 2.0).
- **Rationale**: Next.js offers fast load times, file-based routing, server actions, and Auth.js integration. FastAPI is fast, async-native, uses type validation via Pydantic, and fits the AI/LLM ecosystem.

## ADR 3: JWT Verification Pattern
- **Decision**: PyJWT with symmetric signature key (shared secret) in dev. NextAuth.js on frontend acts as auth manager, delegates Credentials auth to backend `/login` and Google auth details to backend `/google`. Backend issues app JWT.
- **Rationale**: Decouples API security from frontend runtime. PyJWT is currently supported, whereas `python-jose` is deprecated and contains vulnerabilities.

## ADR 4: Database Hashing
- **Decision**: `pwdlib[argon2]`.
- **Rationale**: Replaces `passlib[bcrypt]` as Argon2 is the OWASP recommended password hashing algorithm and pwdlib is active and modern.

## ADR 5: Redis client
- **Decision**: `redis[hiredis]` using `redis.asyncio`.
- **Rationale**: `aioredis` was merged into the official `redis-py` library and is now deprecated. Using the native `redis-py` async API keeps dependencies light.

## ADR 6: Email Verification Trigger
- **Decision**: Resend integration in Phase 1.
- **Rationale**: Immediate email verification enforces high-integrity registration. Resend offers a simple REST API and Python/JS SDKs.
