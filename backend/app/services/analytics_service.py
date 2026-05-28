import uuid
import structlog
from datetime import date
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.execution_metric import ExecutionMetric

logger = structlog.get_logger()

class AnalyticsService:
    def __init__(self):
        pass

    async def calculate_daily_score(self, db: AsyncSession, user_id: uuid.UUID, target_date: date) -> ExecutionMetric:
        """
        Calculates or updates the daily execution score. 
        In production, this queries the tasks completed, flashcards reviewed, and focus sessions.
        """
        logger.info("calculating_daily_score", user_id=user_id, date=target_date)
        
        # Mock calculation: Replace with real DB aggregates
        task_completion = 85.0
        focus_hours = 90.0
        retention = 75.0
        overall = (task_completion * 0.4) + (focus_hours * 0.4) + (retention * 0.2)
        
        result = await db.execute(select(ExecutionMetric).where(
            ExecutionMetric.user_id == user_id, 
            ExecutionMetric.record_date == target_date
        ))
        metric = result.scalars().first()
        
        if metric:
            metric.task_completion_score = task_completion
            metric.focus_hours_score = focus_hours
            metric.retention_score = retention
            metric.overall_score = overall
        else:
            metric = ExecutionMetric(
                user_id=user_id,
                record_date=target_date,
                task_completion_score=task_completion,
                focus_hours_score=focus_hours,
                retention_score=retention,
                overall_score=overall
            )
            db.add(metric)
            
        await db.commit()
        await db.refresh(metric)
        return metric
        
    async def get_weekly_metrics(self, db: AsyncSession, user_id: uuid.UUID) -> List[ExecutionMetric]:
        result = await db.execute(
            select(ExecutionMetric)
            .where(ExecutionMetric.user_id == user_id)
            .order_by(ExecutionMetric.record_date.asc())
            .limit(7)
        )
        return list(result.scalars().all())
