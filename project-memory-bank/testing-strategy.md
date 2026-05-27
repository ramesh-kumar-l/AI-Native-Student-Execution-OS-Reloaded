# Testing Strategy

## Backend Testing
- **Framework**: `pytest` + `pytest-asyncio` for async functions.
- **Database Isolation**: We will use a mock or dedicated test database environment defined in `tests/conftest.py`.
- **Test Strategy**:
  - Unit tests for helpers, utilities, and password hashes.
  - Endpoint integration tests using FastAPI's `TestClient` (via `httpx.AsyncClient`) checking status codes, schema compliance, and database mutations.

## Frontend Testing
- **Framework**: Jest + React Testing Library (for utility classes and state management).
- **Linter**: ESLint strict configurations.
- **Type Safety**: strict TS compilation (`tsc --noEmit`).

## CI Pipeline Integration
Every PR will run:
- Pre-commit checks.
- Backend linting via `ruff`.
- Pytest integration suite execution.
- Frontend linting and typescript compilation checking.
