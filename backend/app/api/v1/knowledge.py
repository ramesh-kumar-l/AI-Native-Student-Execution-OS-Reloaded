from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.flashcard import Flashcard
from app.api.schemas.knowledge import FlashcardResponse, SearchQuery
from app.services.vector_db_service import VectorDBService

router = APIRouter(prefix="/knowledge", tags=["Knowledge"])
vector_db = VectorDBService()

@router.get("/flashcards", response_model=List[FlashcardResponse])
async def get_flashcards(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Flashcard)
        .where(Flashcard.user_id == current_user.id)
        .order_by(Flashcard.next_review_date.asc())
    )
    return list(result.scalars().all())

@router.post("/search")
async def semantic_search(
    query_data: SearchQuery,
    current_user: User = Depends(get_current_user)
):
    results = await vector_db.semantic_search(
        query=query_data.query, 
        user_id=current_user.id,
        n_results=query_data.n_results
    )
    return {"results": results}
