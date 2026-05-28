from typing import Optional, List
from pydantic import BaseModel
import uuid
from datetime import datetime

class DocumentResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    file_path: str
    format: str
    status: str
    page_count: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

class FlashcardResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    document_id: Optional[uuid.UUID]
    front: str
    back: str
    next_review_date: datetime

    class Config:
        from_attributes = True

class SearchQuery(BaseModel):
    query: str
    n_results: int = 5
