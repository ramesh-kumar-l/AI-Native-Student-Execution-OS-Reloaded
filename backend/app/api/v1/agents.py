import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.agent_message import AgentMessage
from app.api.schemas.agents import AgentMessageCreate, AgentMessageResponse
from app.services.agent_orchestrator_service import AgentOrchestratorService

router = APIRouter(prefix="/agents", tags=["Agents"])
orchestrator = AgentOrchestratorService()

@router.get("/{agent_type}/history", response_model=List[AgentMessageResponse])
async def get_agent_history(
    agent_type: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if agent_type not in orchestrator.agents:
        raise HTTPException(status_code=400, detail="Invalid agent type")
        
    result = await db.execute(
        select(AgentMessage)
        .where(AgentMessage.user_id == current_user.id, AgentMessage.agent_type == agent_type)
        .order_by(AgentMessage.created_at.asc())
    )
    return list(result.scalars().all())

@router.post("/{agent_type}/chat", response_model=AgentMessageResponse)
async def chat_with_agent(
    agent_type: str,
    data: AgentMessageCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        response_text = await orchestrator.process_message(
            user_id=current_user.id,
            agent_type=agent_type,
            message=data.message,
            db=db
        )
        
        # Return the newly created agent message for immediate UI update
        result = await db.execute(
            select(AgentMessage)
            .where(AgentMessage.user_id == current_user.id, AgentMessage.role == "agent")
            .order_by(AgentMessage.created_at.desc())
        )
        return result.scalars().first()
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
