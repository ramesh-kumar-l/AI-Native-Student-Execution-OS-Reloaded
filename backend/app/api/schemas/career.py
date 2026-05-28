from typing import Optional, List, Dict
from pydantic import BaseModel
import uuid
from datetime import datetime

class ResumeResponse(BaseModel):
    id: uuid.UUID
    title: str
    content: Dict
    created_at: datetime

    class Config:
        from_attributes = True

class OpportunityCreate(BaseModel):
    company: str
    role: str

class OpportunityUpdateStatus(BaseModel):
    status: str

class OpportunityResponse(BaseModel):
    id: uuid.UUID
    company: str
    role: str
    status: str
    applied_date: Optional[datetime]

    class Config:
        from_attributes = True

class MockInterviewRequest(BaseModel):
    resume_id: uuid.UUID
    opportunity_id: uuid.UUID
