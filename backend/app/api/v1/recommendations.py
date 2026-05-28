import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.recommendation import Recommendation
from app.api.schemas.planning import RecommendationResponse

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/", response_model=List[RecommendationResponse])
async def get_recommendations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Recommendation)
        .where(Recommendation.user_id == current_user.id, Recommendation.is_dismissed == False)
        .order_by(Recommendation.created_at.desc())
    )
    return list(result.scalars().all())

@router.post("/{rec_id}/dismiss", status_code=status.HTTP_204_NO_CONTENT)
async def dismiss_recommendation(
    rec_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Recommendation).where(Recommendation.id == rec_id, Recommendation.user_id == current_user.id))
    rec = result.scalars().first()
    if not rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recommendation not found")
    
    rec.is_dismissed = True
    db.add(rec)
    await db.commit()
