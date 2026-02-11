from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

from app.services.job_ad_service import FacebookJobAdService

app = FastAPI(title="Facebook Job Ad Agent")

service = FacebookJobAdService()

class FacebookJobRequest(BaseModel):
    page_id: str
    jobs: List[Dict]

@app.post("/jobs/facebook")
def post_facebook_jobs(payload: FacebookJobRequest):
    try:
        result = service.create_and_post(
            page_id=payload.page_id,
            job_data=payload.jobs
        )
        return {
            "status": "success",
            "formatted_post": result["ad_text"],
            "facebook_response": result["facebook_response"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))