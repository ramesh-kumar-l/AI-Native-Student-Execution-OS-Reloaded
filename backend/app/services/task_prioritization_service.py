import os
import structlog
from typing import List
from google import genai
from google.genai import types
from app.models.task import Task
from app.core.config import get_settings

logger = structlog.get_logger()
settings = get_settings()

class TaskPrioritizationService:
    def __init__(self):
        # In a real setup, api_key would be passed from settings.
        self.client = genai.Client() if os.getenv("GEMINI_API_KEY") else None

    async def prioritize_tasks(self, tasks: List[Task]) -> List[Task]:
        if not self.client:
            logger.warn("gemini_api_key_missing_fallback_to_heuristic")
            return self._heuristic_prioritization(tasks)

        prompt = self._build_prompt(tasks)
        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            return self._parse_and_apply_scores(tasks, response.text)
        except Exception as e:
            logger.error("gemini_api_call_failed", error=str(e))
            return self._heuristic_prioritization(tasks)

    def _build_prompt(self, tasks: List[Task]) -> str:
        prompt = "You are an AI planner. Score these tasks from 0 to 100 on urgency and importance.\n"
        for t in tasks:
            prompt += f"ID: {t.id} | Title: {t.title} | Deadline: {t.deadline}\n"
        prompt += "Return CSV format: task_id,score\n"
        return prompt

    def _parse_and_apply_scores(self, tasks: List[Task], response_text: str) -> List[Task]:
        # Basic parser for CSV format
        scores = {}
        for line in response_text.strip().split('\n'):
            parts = line.split(',')
            if len(parts) == 2:
                try:
                    scores[parts[0].strip()] = float(parts[1].strip())
                except ValueError:
                    pass
        
        for task in tasks:
            task_id_str = str(task.id)
            if task_id_str in scores:
                task.priority_score = scores[task_id_str]
        
        # Sort tasks by priority descending
        return sorted(tasks, key=lambda x: x.priority_score, reverse=True)

    def _heuristic_prioritization(self, tasks: List[Task]) -> List[Task]:
        # Fallback if no API key: closest deadline first
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        
        for task in tasks:
            if task.deadline:
                days_left = (task.deadline - now).days
                task.priority_score = max(0.0, 100.0 - (max(days_left, 0) * 5.0))
            else:
                task.priority_score = 50.0
                
        return sorted(tasks, key=lambda x: x.priority_score, reverse=True)
