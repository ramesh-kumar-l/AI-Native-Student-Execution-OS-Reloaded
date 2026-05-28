# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app
RUN pip install uv

COPY pyproject.toml .
RUN uv pip install --system -r pyproject.toml

# Production stage
FROM python:3.12-slim

WORKDIR /app

# Copy python dependencies
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY . .

# Run as non-root user
RUN useradd -m appuser \
    && mkdir -p /app/uploads \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
