from pydantic import BaseModel
from typing import Literal, Optional

class AvailabilityResponse(BaseModel):
  intent: Literal["accepted", "rejected", "reschedule", "invalid"]
  option: Optional[str] = None