import os
import structlog
from google import genai
from typing import List

logger = structlog.get_logger()

class InterviewSimulatorService:
    def __init__(self):
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None

    async def generate_mock_questions(self, role: str, company: str, resume_json: dict) -> List[str]:
        """
        Generates personalized interview questions based on the target role and user's resume.
        """
        if not self.client:
            logger.warn("gemini_api_key_missing_interview_questions_mocked")
            return [
                f"Why do you want to work at {company}?",
                f"Tell me about a time you showed leadership.",
                f"How would you approach a technical problem in {role}?"
            ]

        prompt = (
            f"You are an expert technical recruiter at {company} hiring for a {role}. "
            "Based on the following JSON resume of the candidate, generate 3 highly targeted interview questions "
            "(1 behavioral, 1 technical, 1 role-specific). Output each question on a new line.\n\n"
            f"RESUME JSON:\n{resume_json}"
        )

        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            return [line.strip() for line in response.text.strip().split('\n') if line.strip()]
        except Exception as e:
            logger.error("interview_generation_failed", error=str(e))
            return ["Failed to generate questions. Please try again."]
