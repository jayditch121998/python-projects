from pydantic import BaseModel, Field
from typing import List

class JobDetails(BaseModel):
    role: str = Field(..., min_length=2)
    company_name: str
    location: str
    experience: str
    skills: List[str]
    responsibilities: List[str]
    benefits: List[str]
    apply_link: str