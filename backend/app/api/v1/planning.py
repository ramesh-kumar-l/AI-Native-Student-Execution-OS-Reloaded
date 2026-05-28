import uuid
from datetime import datetime, timezone, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.task import Task
from app.models.calendar import CalendarEvent
from app.api.schemas.planning import StudyBlockResponse
from app.services.task_prioritization_service import TaskPrioritizationService
from app.services.study_planner_service import StudyPlannerService

router = APIRouter(prefix="/planning", tags=["Planning"])
task_service = TaskPrioritizationService()
planner_service = StudyPlannerService()

@router.post("/generate", response_model=List[StudyBlockResponse])
async def generate_plan(
    days_ahead: int = 3,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Fetch tasks
    tasks_result = await db.execute(select(Task).where(Task.user_id == current_user.id, Task.status != "done"))
    tasks = list(tasks_result.scalars().all())
    
    if not tasks:
        return []

    # AI Prioritization
    prioritized_tasks = await task_service.prioritize_tasks(tasks)
    
    # Save new scores
    db.add_all(prioritized_tasks)
    
    # Fetch calendar events
    start_date = datetime.now(timezone.utc)
    end_date = start_date + timedelta(days=days_ahead)
    events_result = await db.execute(
        select(CalendarEvent)
        .where(CalendarEvent.user_id == current_user.id)
        .where(CalendarEvent.end_time >= start_date)
        .where(CalendarEvent.start_time <= end_date)
    )
    events = list(events_result.scalars().all())

    # Generate Blocks
    blocks = await planner_service.generate_study_plan(current_user.id, prioritized_tasks, events, start_date, end_date)
    
    # Save blocks
    if blocks:
        db.add_all(blocks)
    
    await db.commit()
    return blocks
