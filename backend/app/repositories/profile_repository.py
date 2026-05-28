import uuid
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.student_profile import StudentProfile
from app.api.schemas.profile import StudentProfileCreate, StudentProfileUpdate

class ProfileRepository:
    async def get_by_user_id(self, db: AsyncSession, user_id: uuid.UUID) -> Optional[StudentProfile]:
        result = await db.execute(select(StudentProfile).where(StudentProfile.user_id == user_id))
        return result.scalars().first()

    async def create(self, db: AsyncSession, user_id: uuid.UUID, data: StudentProfileCreate) -> StudentProfile:
        db_obj = StudentProfile(user_id=user_id, **data.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, db_obj: StudentProfile, data: StudentProfileUpdate) -> StudentProfile:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
