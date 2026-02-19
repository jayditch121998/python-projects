from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.db.session import SessionLocal
from app.models.booking_session import BookingSession, BookingState

class SlotAlreadyTakenException(Exception):
  pass

class BookingService:
  def createSession(self, email: str):
    db: Session = SessionLocal()
    try:
      session = BookingSession(
        email=email,
        state=BookingState.GENERATING_SLOTS
      )
      db.add(session)
      db.commit()
      db.refresh(session)
      return session
    finally:
      db.close
      
  def reserveSlot(self, sessionId, start: datetime, end: datetime):
    db: Session = SessionLocal()
    try:
      session = db.query(BookingSession).filter(
        BookingSession.id == sessionId
      ).first()
      
      if not session:
        raise Exception("Session not found")
      
      session.selected_slot_start = start
      session.selected_slot_end = end
      session.state = BookingState.BOOKING
      
      db.commit()
      
    except IntegrityError:
      db.rollback()
      raise SlotAlreadyTakenException("Slot already reserved")
    
    finally:
      db.close()