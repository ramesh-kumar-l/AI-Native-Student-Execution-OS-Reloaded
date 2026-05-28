from typing import Optional, List
from pydantic import BaseModel
import uuid
from datetime import datetime

class CalendarSourceBase(BaseModel):
    name: str
    url: str

class CalendarSourceCreate(CalendarSourceBase):
    pass

class CalendarSourceUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    is_active: Optional[bool] = None

class CalendarSourceResponse(CalendarSourceBase):
    id: uuid.UUID
    user_id: uuid.UUID
    is_active: bool
    last_synced_at: Optional[datetime]
    sync_error: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CalendarEventResponse(BaseModel):
    id: uuid.UUID
    source_id: uuid.UUID
    user_id: uuid.UUID
    external_id: str
    title: str
    description: Optional[str]
    location: Optional[str]
    start_time: datetime
    end_time: datetime
    is_all_day: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
