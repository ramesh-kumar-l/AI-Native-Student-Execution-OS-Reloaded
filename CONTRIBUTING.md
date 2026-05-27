# Contributing Guidelines

Welcome to the AI-Native Student Execution OS project! Thank you for contributing. To ensure high-quality execution and keep cognitive token costs low, please follow these conventions:

## Code & Quality Standards

- **Strict Type Safety**: All TypeScript files must compile with strict compiler settings. All Python files must use explicit type annotations.
- **Structured Log Messages**: Always use `structlog` for logging in the backend. Do not use standard `print()` or untraced log outputs.
- **Fail-Safe Integrity**: Ensure database schemas and models are completely verified using migration files (`alembic`). Never commit direct DB manipulations.
- **API and Data Models**: Do not expose raw SQLAlchemy models in routers. Always define input/output schemas using Pydantic.

---

## Memory Bank Coordination

This project relies on `project-memory-bank/` as a persistent coordination layer for agents and developers.

Before starting any task:
1. Review `active-context.md` and `implementation-status.md`.
2. Do not refactor stable files unless specified.
3. Update `task-history.md`, `implementation-status.md`, and `active-context.md` at the end of every work session.
