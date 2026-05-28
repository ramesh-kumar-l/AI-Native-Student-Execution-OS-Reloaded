import uuid
import structlog
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.opportunity import Opportunity

logger = structlog.get_logger()

class OpportunityService:
    def __init__(self):
        pass

    async def create_opportunity(self, db: AsyncSession, user_id: uuid.UUID, company: str, role: str) -> Opportunity:
        logger.info("creating_opportunity", user_id=user_id, company=company)
        opp = Opportunity(
            user_id=user_id,
            company=company,
            role=role,
            status="wishlist"
        )
        db.add(opp)
        await db.commit()
        await db.refresh(opp)
        return opp

    async def update_status(self, db: AsyncSession, opp_id: uuid.UUID, user_id: uuid.UUID, new_status: str) -> Opportunity:
        logger.info("updating_opportunity_status", opp_id=opp_id, new_status=new_status)
        result = await db.execute(select(Opportunity).where(Opportunity.id == opp_id, Opportunity.user_id == user_id))
        opp = result.scalars().first()
        if opp:
            opp.status = new_status
            db.add(opp)
            await db.commit()
            await db.refresh(opp)
        return opp
