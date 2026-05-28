import structlog
from typing import List
from app.models.task import Task
from app.models.student_profile import StudentProfile

logger = structlog.get_logger()

class WorkloadBalancerService:
    def __init__(self):
        pass

    async def calculate_daily_fatigue_limit(self, profile: StudentProfile) -> float:
        """
        Calculate maximum fatigue units a student can handle per day based on their preferences.
        """
        base_limit = 100.0
        
        if profile and profile.preferences:
            max_study_hours = profile.preferences.get("max_study_hours_per_day", 4)
            # Roughly 25 fatigue points per hour of study
            base_limit = max_study_hours * 25.0
            
        logger.info("fatigue_limit_calculated", user_id=profile.user_id, limit=base_limit)
        return base_limit

    async def split_large_tasks(self, tasks: List[Task], max_duration_minutes: int = 120) -> List[Task]:
        """
        Identify tasks that exceed the max duration and recommend splitting them.
        In a real scenario, this would alter the DB or return sub-tasks.
        """
        split_tasks = []
        for task in tasks:
            if task.estimated_duration_minutes > max_duration_minutes:
                logger.info("task_exceeds_max_duration", task_id=task.id)
                # Logic to chunk task into pomodoro sessions
            split_tasks.append(task)
            
        return split_tasks
