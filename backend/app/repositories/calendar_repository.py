import uuid
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.calendar import CalendarSource, CalendarEvent
from app.api.schemas.calendar import CalendarSourceCreate, CalendarSourceUpdate

class CalendarRepository:
    async def get_sources_by_user(self, db: AsyncSession, user_id: uuid.UUID) -> List[CalendarSource]:
        result = await db.execute(select(CalendarSource).where(CalendarSource.user_id == user_id))
        return list(result.scalars().all())

    async def get_source_by_id(self, db: AsyncSession, source_id: uuid.UUID) -> Optional[CalendarSource]:
        result = await db.execute(select(CalendarSource).where(CalendarSource.id == source_id))
        return result.scalars().first()

    async def create_source(self, db: AsyncSession, user_id: uuid.UUID, data: CalendarSourceCreate) -> CalendarSource:
        db_obj = CalendarSource(user_id=user_id, **data.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_source(self, db: AsyncSession, db_obj: CalendarSource, data: CalendarSourceUpdate) -> CalendarSource:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
            
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete_source(self, db: AsyncSession, db_obj: CalendarSource) -> None:
        await db.delete(db_obj)
        await db.commit()

    async def get_events_for_user(self, db: AsyncSession, user_id: uuid.UUID) -> List[CalendarEvent]:
        result = await db.execute(select(CalendarEvent).where(CalendarEvent.user_id == user_id).order_by(CalendarEvent.start_time))
        return list(result.scalars().all())
