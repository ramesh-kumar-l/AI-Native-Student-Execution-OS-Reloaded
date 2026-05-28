import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    deadline: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    estimated_duration_minutes: Mapped[int] = mapped_column(Integer, default=60)
    actual_duration_minutes: Mapped[int] = mapped_column(Integer, default=0)
    
    # Priority scored by AI (0 to 100)
    priority_score: Mapped[float] = mapped_column(Float, default=50.0)
    status: Mapped[str] = mapped_column(String(50), default="todo") # todo, in_progress, done
    
    # Cost to student fatigue (0 to 100)
    fatigue_cost: Mapped[float] = mapped_column(Float, default=10.0)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = relationship("User", backref="tasks")
    study_blocks = relationship("StudyBlock", back_populates="task", cascade="all, delete-orphan")
