from agno.agent import Agent
from app.models.availability_model import AvailabilityResponse

availability_agent = Agent(
  name="Availability Confirmation Agent",
  model="openai:gpt-4o-mini",
  instructions="""
  You analyze a user's reply to availability options.

  Valid options:
  - Option 1
  - Option 2
  - Option 3

  Return JSON:
  {
    "intent": "accepted | rejected | reschedule | invalid",
    "option": "Option 1 | Option 2 | Option 3 | null"
  }

  Rules:
  - If user selects one of the options → intent = accepted
  - If user declines all → intent = rejected
  - If user asks for another time → intent = reschedule
  - If unclear → intent = invalid
  """
)