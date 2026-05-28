import uuid
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models.goal import Goal, Milestone
from app.api.schemas.goal import GoalCreate, GoalUpdate, MilestoneCreate, MilestoneUpdate

class GoalRepository:
    async def get_all_for_user(self, db: AsyncSession, user_id: uuid.UUID) -> List[Goal]:
        result = await db.execute(
            select(Goal)
            .where(Goal.user_id == user_id)
            .options(selectinload(Goal.milestones))
            .order_by(Goal.created_at.desc())
        )
        return list(result.scalars().all())

    async def get_by_id(self, db: AsyncSession, goal_id: uuid.UUID) -> Optional[Goal]:
        result = await db.execute(
            select(Goal).where(Goal.id == goal_id).options(selectinload(Goal.milestones))
        )
        return result.scalars().first()

    async def create_goal(self, db: AsyncSession, user_id: uuid.UUID, data: GoalCreate) -> Goal:
        db_obj = Goal(user_id=user_id, **data.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_goal(self, db: AsyncSession, db_obj: Goal, data: GoalUpdate) -> Goal:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete_goal(self, db: AsyncSession, db_obj: Goal) -> None:
        await db.delete(db_obj)
        await db.commit()

    async def create_milestone(self, db: AsyncSession, goal_id: uuid.UUID, data: MilestoneCreate) -> Milestone:
        db_obj = Milestone(goal_id=goal_id, **data.model_dump())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update_milestone(self, db: AsyncSession, milestone_id: uuid.UUID, data: MilestoneUpdate) -> Optional[Milestone]:
        result = await db.execute(select(Milestone).where(Milestone.id == milestone_id))
        db_obj = result.scalars().first()
        if not db_obj:
            return None
        
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
            
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
