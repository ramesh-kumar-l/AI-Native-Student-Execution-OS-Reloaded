import os
import structlog
from typing import List, Dict
from google import genai

logger = structlog.get_logger()

class BaseAgent:
    def __init__(self, system_instruction: str):
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None
        self.system_instruction = system_instruction

    async def generate_response(self, prompt: str, context: str = "") -> str:
        if not self.client:
            logger.warn("gemini_api_key_missing_agent_response_mocked")
            return f"[Mock {self.__class__.__name__}]: I received your message: '{prompt}'."
            
        full_prompt = f"{self.system_instruction}\n\nCONTEXT:\n{context}\n\nUSER:\n{prompt}"
        
        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=full_prompt,
            )
            return response.text
        except Exception as e:
            logger.error("agent_generation_failed", error=str(e))
            return "Sorry, I'm having trouble thinking right now."

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction="You are 'The Planner', an AI execution agent focused strictly on time management, schedule optimization, and breaking down large tasks. You are concise and direct."
        )

class RevisionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction="You are 'The Revision Master', an AI execution agent focused on memory retention and active recall. You quiz the user based on their context and provide mental models."
        )

class AccountabilityAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction="You are 'The Coach', an AI execution agent focused on accountability and motivation. You are tough but fair. You check in on their goals and streak."
        )
