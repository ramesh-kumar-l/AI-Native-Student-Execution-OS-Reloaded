import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_db, get_current_user
from app.models.user import User
from app.api.schemas.calendar import CalendarSourceCreate, CalendarSourceUpdate, CalendarSourceResponse, CalendarEventResponse
from app.repositories.calendar_repository import CalendarRepository
# from app.services.calendar_service import sync_calendar_source

router = APIRouter(prefix="/calendar", tags=["Calendar"])
calendar_repo = CalendarRepository()

@router.get("/sources", response_model=List[CalendarSourceResponse])
async def get_calendar_sources(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await calendar_repo.get_sources_by_user(db, current_user.id)

@router.post("/sources", response_model=CalendarSourceResponse)
async def create_calendar_source(
    data: CalendarSourceCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    source = await calendar_repo.create_source(db, current_user.id, data)
    # background_tasks.add_task(sync_calendar_source, db, source.id)
    return source

@router.put("/sources/{source_id}", response_model=CalendarSourceResponse)
async def update_calendar_source(
    source_id: uuid.UUID,
    data: CalendarSourceUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    source = await calendar_repo.get_source_by_id(db, source_id)
    if not source or source.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Source not found")
    return await calendar_repo.update_source(db, source, data)

@router.delete("/sources/{source_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_calendar_source(
    source_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    source = await calendar_repo.get_source_by_id(db, source_id)
    if not source or source.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Source not found")
    await calendar_repo.delete_source(db, source)

@router.get("/events", response_model=List[CalendarEventResponse])
async def get_calendar_events(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await calendar_repo.get_events_for_user(db, current_user.id)
