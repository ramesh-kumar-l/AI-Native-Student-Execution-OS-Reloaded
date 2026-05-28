from typing import Optional, List
from pydantic import BaseModel
import uuid
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    estimated_duration_minutes: int = 60
    status: str = "todo"

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    priority_score: float
    fatigue_cost: float
    actual_duration_minutes: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class StudyBlockResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    task_id: Optional[uuid.UUID]
    title: str
    start_time: datetime
    end_time: datetime
    generated_by_ai: bool
    is_completed: bool

    class Config:
        from_attributes = True

class RecommendationResponse(BaseModel):
    id: uuid.UUID
    message: str
    action_type: str
    target_id: Optional[str]
    is_dismissed: bool
    is_actioned: bool

    class Config:
        from_attributes = True
