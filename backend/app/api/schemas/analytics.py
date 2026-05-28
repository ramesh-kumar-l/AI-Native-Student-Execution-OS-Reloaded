from typing import List, Optional
from pydantic import BaseModel
import uuid
from datetime import date, datetime

class ExecutionMetricResponse(BaseModel):
    id: uuid.UUID
    record_date: date
    task_completion_score: float
    focus_hours_score: float
    retention_score: float
    overall_score: float

    class Config:
        from_attributes = True

class ReflectionResponse(BaseModel):
    id: uuid.UUID
    period_type: str
    ai_insights: str
    user_notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
