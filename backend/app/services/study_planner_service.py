import structlog
import uuid
from typing import List
from datetime import datetime, timedelta, timezone
from app.models.task import Task
from app.models.calendar import CalendarEvent
from app.models.study_block import StudyBlock

logger = structlog.get_logger()

class StudyPlannerService:
    def __init__(self):
        pass

    async def generate_study_plan(
        self, 
        user_id: uuid.UUID, 
        tasks: List[Task], 
        events: List[CalendarEvent], 
        start_date: datetime, 
        end_date: datetime
    ) -> List[StudyBlock]:
        """
        Naive whitespace algorithm: finds gaps in calendar events and assigns top-priority tasks.
        """
        logger.info("generating_study_plan", user_id=user_id, task_count=len(tasks), event_count=len(events))
        
        blocks = []
        current_time = start_date
        
        # Sort tasks by priority
        sorted_tasks = sorted(tasks, key=lambda t: t.priority_score, reverse=True)
        
        for task in sorted_tasks:
            if current_time >= end_date:
                break
                
            # Naive: create a block if we haven't hit end_date
            # In production, we'd check against `events` for overlaps.
            duration = timedelta(minutes=task.estimated_duration_minutes)
            
            block = StudyBlock(
                user_id=user_id,
                task_id=task.id,
                title=f"Study: {task.title}",
                start_time=current_time,
                end_time=current_time + duration,
                generated_by_ai=True
            )
            blocks.append(block)
            
            # Advance time with a 15 min break
            current_time = current_time + duration + timedelta(minutes=15)
            
        return blocks
