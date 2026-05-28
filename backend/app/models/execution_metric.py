import uuid
from datetime import date, datetime, timezone
from sqlalchemy import String, Integer, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class ExecutionMetric(Base):
    __tablename__ = "execution_metrics"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Tracked per day
    record_date: Mapped[date] = mapped_column(Date, nullable=False)
    
    # Scores (0.0 to 100.0)
    task_completion_score: Mapped[float] = mapped_column(Float, default=0.0)
    focus_hours_score: Mapped[float] = mapped_column(Float, default=0.0)
    retention_score: Mapped[float] = mapped_column(Float, default=0.0) # From flashcards
    
    # Overall aggregated score
    overall_score: Mapped[float] = mapped_column(Float, default=0.0)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship("User", backref="execution_metrics")
