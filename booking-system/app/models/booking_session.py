import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, String, DateTime, Enum, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

class BookingState(str, PyEnum):
  GENERATING_SLOTS = "generatingSlots"
  AWAITING_SELECTION = "awaitingSelection"
  VALIDATING_SLOT = "validatingSlot"
  BOOKING = "booking"
  COMPLETED = "completed"
  CONFLICT = "conflict"
  EXPIRED = "expired"
  
class BookingSession(Base):
  __tablename__ = "booking_sessions"
  
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  email = Column(String, nullable=False)
  state = Column(Enum(BookingState), nullable=False)

  selected_slot_start = Column(DateTime, nullable=True)
  selected_slot_end = Column(DateTime, nullable=True)

  expires_at = Column(DateTime, nullable=True)

  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow)

  __table_args__ = (
      UniqueConstraint(
          "selected_slot_start",
          "selected_slot_end",
          name="unique_slot_constraint"
      ),
  )
  