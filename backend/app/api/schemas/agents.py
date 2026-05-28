from typing import List
from pydantic import BaseModel
import uuid
from datetime import datetime

class AgentMessageCreate(BaseModel):
    message: str

class AgentMessageResponse(BaseModel):
    id: uuid.UUID
    agent_type: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
