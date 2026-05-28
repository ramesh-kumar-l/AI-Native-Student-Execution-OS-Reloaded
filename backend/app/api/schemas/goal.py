from typing import Optional, List
from pydantic import BaseModel
import uuid
from datetime import datetime

class MilestoneBase(BaseModel):
    title: str
    is_completed: bool = False
    target_date: Optional[datetime] = None

class MilestoneCreate(MilestoneBase):
    pass

class MilestoneUpdate(MilestoneBase):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class MilestoneResponse(MilestoneBase):
    id: uuid.UUID
    goal_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    target_date: Optional[datetime] = None

class GoalCreate(GoalBase):
    pass

class GoalUpdate(GoalBase):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class GoalResponse(GoalBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    milestones: List[MilestoneResponse] = []

    class Config:
        from_attributes = True
