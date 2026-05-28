import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.resume import Resume
from app.models.opportunity import Opportunity
from app.api.schemas.career import ResumeResponse, OpportunityCreate, OpportunityUpdateStatus, OpportunityResponse, MockInterviewRequest
from app.services.resume_service import ResumeService
from app.services.opportunity_service import OpportunityService
from app.services.interview_simulator_service import InterviewSimulatorService

router = APIRouter(prefix="/career", tags=["Career"])

resume_service = ResumeService()
opp_service = OpportunityService()
interview_service = InterviewSimulatorService()

@router.get("/opportunities", response_model=List[OpportunityResponse])
async def get_opportunities(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Opportunity).where(Opportunity.user_id == current_user.id))
    return list(result.scalars().all())

@router.post("/opportunities", response_model=OpportunityResponse)
async def create_opportunity(
    data: OpportunityCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await opp_service.create_opportunity(db, current_user.id, data.company, data.role)

@router.patch("/opportunities/{opp_id}/status", response_model=OpportunityResponse)
async def update_opportunity_status(
    opp_id: uuid.UUID,
    data: OpportunityUpdateStatus,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    opp = await opp_service.update_status(db, opp_id, current_user.id, data.status)
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opp

@router.post("/mock-interview")
async def generate_mock_interview(
    data: MockInterviewRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Fetch Resume
    res_result = await db.execute(select(Resume).where(Resume.id == data.resume_id, Resume.user_id == current_user.id))
    resume = res_result.scalars().first()
    
    # Fetch Opportunity
    opp_result = await db.execute(select(Opportunity).where(Opportunity.id == data.opportunity_id, Opportunity.user_id == current_user.id))
    opp = opp_result.scalars().first()
    
    if not resume or not opp:
        raise HTTPException(status_code=404, detail="Resume or Opportunity not found")
        
    questions = await interview_service.generate_mock_questions(opp.role, opp.company, resume.content)
    return {"questions": questions}
