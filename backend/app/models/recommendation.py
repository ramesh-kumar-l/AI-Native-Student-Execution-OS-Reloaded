import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", on_delete="CASCADE"), nullable=False)
    
    message: Mapped[str] = mapped_column(String(2000), nullable=False)
    action_type: Mapped[str] = mapped_column(String(100), nullable=False) # e.g. "shift_task", "take_break"
    target_id: Mapped[str | None] = mapped_column(String(255), nullable=True) # UUID of related entity
    
    is_dismissed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_actioned: Mapped[bool] = mapped_column(Boolean, default=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship("User", backref="recommendations")
