import json
from app.agents.availability_agent import availability_agent


def process_availability(message: str):
  result = availability_agent.run(message)

  try:
    return json.loads(result.content)
  except Exception:
    return {
      "intent": "invalid",
      "option": None
    }
