import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_liveness_check(client: AsyncClient):
    response = await client.get("/api/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

@pytest.mark.asyncio
async def test_readiness_check_healthy(client: AsyncClient):
    response = await client.get("/api/health/ready")
    # Should return ready since database and redis are mock/overridden or stubbed
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["checks"]["database"] == "healthy"
    assert data["checks"]["redis"] == "healthy"
