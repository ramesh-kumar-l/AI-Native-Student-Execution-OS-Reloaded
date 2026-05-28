import os
import structlog
from typing import List
from google import genai
from app.models.document import Document
from app.models.flashcard import Flashcard

logger = structlog.get_logger()

class KnowledgeExtractionService:
    def __init__(self):
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None

    async def generate_flashcards(self, text: str, document: Document, count: int = 5) -> List[Flashcard]:
        """
        Generates high-yield flashcards from the provided text using Gemini.
        """
        if not self.client:
            logger.warn("gemini_api_key_missing_flashcard_generation_skipped")
            # Fallback for local testing without key
            return [
                Flashcard(
                    user_id=document.user_id,
                    document_id=document.id,
                    front=f"Mock Question {i}",
                    back=f"Mock Answer {i}"
                ) for i in range(count)
            ]

        prompt = (
            f"You are an expert tutor. Create {count} high-yield flashcards from the following text.\n"
            "Output exactly in this format, separated by newlines:\n"
            "Q: [Question]\nA: [Answer]\n\n"
            f"TEXT:\n{text[:10000]}" # Truncate for token limits in this naive implementation
        )

        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            return self._parse_flashcards(response.text, document)
        except Exception as e:
            logger.error("flashcard_generation_failed", error=str(e))
            return []

    def _parse_flashcards(self, response_text: str, document: Document) -> List[Flashcard]:
        flashcards = []
        lines = response_text.strip().split('\n')
        
        current_q = None
        for line in lines:
            line = line.strip()
            if line.startswith("Q:"):
                current_q = line[2:].strip()
            elif line.startswith("A:") and current_q:
                current_a = line[2:].strip()
                flashcards.append(Flashcard(
                    user_id=document.user_id,
                    document_id=document.id,
                    front=current_q,
                    back=current_a
                ))
                current_q = None
                
        return flashcards

    async def generate_summary(self, text: str) -> str:
        """
        Generates a concise mental model summary.
        """
        if not self.client:
            return "Mock summary because Gemini API key is missing."
            
        prompt = "Summarize the following text into 3 key takeaways/mental models:\n\n" + text[:10000]
        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            logger.error("summary_generation_failed", error=str(e))
            return "Failed to generate summary."
