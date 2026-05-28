import os
import structlog
from google import genai
from typing import Dict

logger = structlog.get_logger()

class ResumeService:
    def __init__(self):
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None

    async def parse_resume_to_json(self, raw_text: str) -> Dict:
        """
        Parses raw text (from PDF/TXT) into a standardized JSON resume structure.
        """
        if not self.client:
            logger.warn("gemini_api_key_missing_resume_parsing_mocked")
            return {"basics": {"name": "Mock Name", "summary": "Mock summary parsed from text."}}

        prompt = (
            "Extract the following raw resume text into a strict JSON object following the JSON Resume schema format. "
            "Include sections for basics (name, email, summary), work, education, and skills. "
            "Return ONLY valid JSON, no markdown formatting.\n\n"
            f"RAW TEXT:\n{raw_text[:8000]}"
        )

        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            import json
            # Clean possible markdown wrap
            cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned_text)
        except Exception as e:
            logger.error("resume_parsing_failed", error=str(e))
            return {"basics": {"name": "Error Parsing", "summary": str(e)}}
