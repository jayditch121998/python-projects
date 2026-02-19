from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.models import booking_session
from datetime import datetime
from app.services.booking_service import BookingService, SlotAlreadyTakenException
# docker run --name booking-postgres -e POSTGRES_USER=booking -e POSTGRES_PASSWORD=booking123 -e POSTGRES_DB=bookingdb -p 5432:5432 -d postgres
app = FastAPI()
service = BookingService()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
  return {"status": "Booking engine running"}

@app.post("/test-reserve")
def test_reserve(email: str, start: str, end: str):
  try:
    session = service.createSession(email)
    service.reserveSlot(
      session.id,
      datetime.fromisoformat(start),
      datetime.fromisoformat(end)
    )
    return {"status": "reserved"}
  
  except SlotAlreadyTakenException:
    raise HTTPException(status_code=400, details="Slot already taken")