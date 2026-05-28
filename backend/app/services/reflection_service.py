import os
import uuid
import structlog
from google import genai
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.reflection import Reflection
from app.models.execution_metric import ExecutionMetric

logger = structlog.get_logger()

class ReflectionService:
    def __init__(self):
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None

    async def generate_weekly_reflection(self, db: AsyncSession, user_id: uuid.UUID, metrics: list[ExecutionMetric]) -> Reflection:
        """
        Generates AI insights based on the week's execution scores.
        """
        if not self.client:
            logger.warn("gemini_api_key_missing_reflection_mocked")
            insights = "You had a solid week, but your focus scores dipped on Thursday. Try to allocate more deep work blocks."
        else:
            # Construct context from metrics
            metrics_context = "\n".join([f"Date: {m.record_date}, Overall Score: {m.overall_score:.1f}, Task Completion: {m.task_completion_score:.1f}, Focus: {m.focus_hours_score:.1f}, Retention: {m.retention_score:.1f}" for m in metrics])
            
            prompt = (
                "You are an elite execution coach. Review the following weekly metrics for the user and provide a harsh but fair 3-sentence reflection "
                "highlighting where they succeeded and where they slacked off.\n\n"
                f"METRICS:\n{metrics_context}"
            )
            
            try:
                response = self.client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=prompt,
                )
                insights = response.text.strip()
            except Exception as e:
                logger.error("reflection_generation_failed", error=str(e))
                insights = "Failed to generate reflection."
                
        reflection = Reflection(
            user_id=user_id,
            period_type="weekly",
            ai_insights=insights
        )
        db.add(reflection)
        await db.commit()
        await db.refresh(reflection)
        return reflection
