import uuid
import structlog
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.agent_message import AgentMessage
from app.services.agents import PlannerAgent, RevisionAgent, AccountabilityAgent

logger = structlog.get_logger()

class AgentOrchestratorService:
    def __init__(self):
        self.agents = {
            "planner": PlannerAgent(),
            "revision": RevisionAgent(),
            "accountability": AccountabilityAgent()
        }

    async def process_message(
        self, 
        user_id: uuid.UUID, 
        agent_type: str, 
        message: str, 
        db: AsyncSession
    ) -> str:
        """
        Routes a user message to the correct agent persona, fetches context, and saves interaction.
        """
        if agent_type not in self.agents:
            raise ValueError(f"Unknown agent type: {agent_type}")
            
        logger.info("processing_agent_message", user_id=user_id, agent_type=agent_type)
        
        # 1. Save user message
        user_msg = AgentMessage(
            user_id=user_id,
            agent_type=agent_type,
            role="user",
            content=message
        )
        db.add(user_msg)
        await db.commit()
        
        # 2. Fetch context (naive context fetching for now)
        # In production, we'd fetch actual tasks/flashcards here based on the agent_type.
        context_data = "You are currently interacting with the user's execution environment."
        
        # 3. Generate Agent Response
        agent = self.agents[agent_type]
        response_text = await agent.generate_response(message, context_data)
        
        # 4. Save agent message
        agent_msg = AgentMessage(
            user_id=user_id,
            agent_type=agent_type,
            role="agent",
            content=response_text
        )
        db.add(agent_msg)
        await db.commit()
        
        return response_text
