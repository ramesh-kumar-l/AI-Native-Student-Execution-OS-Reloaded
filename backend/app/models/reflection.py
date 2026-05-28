import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Reflection(Base):
    __tablename__ = "reflections"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Period: 'daily', 'weekly', 'monthly'
    period_type: Mapped[str] = mapped_column(String(50), default="weekly")
    
    # AI generated insights
    ai_insights: Mapped[str] = mapped_column(Text, nullable=False)
    
    # User's own journal entry
    user_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship("User", backref="reflections")
