from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date
from app.api.dependencies import get_db, get_current_user
from app.models.user import User
from app.api.schemas.analytics import ExecutionMetricResponse, ReflectionResponse
from app.services.analytics_service import AnalyticsService
from app.services.reflection_service import ReflectionService

router = APIRouter(prefix="/analytics", tags=["Analytics"])

analytics_service = AnalyticsService()
reflection_service = ReflectionService()

@router.post("/calculate-daily", response_model=ExecutionMetricResponse)
async def calculate_daily(
    target_date: date = date.today(),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await analytics_service.calculate_daily_score(db, current_user.id, target_date)

@router.get("/metrics", response_model=List[ExecutionMetricResponse])
async def get_metrics(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await analytics_service.get_weekly_metrics(db, current_user.id)

@router.post("/generate-reflection", response_model=ReflectionResponse)
async def generate_reflection(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    metrics = await analytics_service.get_weekly_metrics(db, current_user.id)
    return await reflection_service.generate_weekly_reflection(db, current_user.id, metrics)
