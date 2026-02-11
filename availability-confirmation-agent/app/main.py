import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.services.availability_service import process_availability

load_dotenv()
print("OPENAI KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))
app = FastAPI(title="Availability Confirmation Agent")

@app.post("/availability")
async def check_availability(payload: dict):
  message = payload.get("message")
  
  if not message:
    return {"error": "Message is required"}
  
  return process_availability(message)