from agno.agent import Agent
from agno.models.openai import OpenAIChat
from app.schemas.job_details import JobDetails
from app.config.settings import settings
from instructions.system_prompt import SYSTEM_PROMPT_TEXT

class JobFormatterAgent:
  def __init__(self):
    self.agent = Agent(
      name="Job Ad Formatter",
      model=OpenAIChat(id=settings.OPENAI_MODEL),
      instructions=SYSTEM_PROMPT_TEXT,
      markdown=True
    )
  
  def format(self, valid_jobs: list[dict]) -> str:
        user_prompt = self.build_user_prompt(valid_jobs)
        result = self.agent.run(user_prompt)
        return result.content
  
  
  def build_user_prompt(self, valid_jobs: list[dict]) -> str:
    job_blocks = []
    print(valid_jobs)
    for i, job in enumerate(valid_jobs):
        print("TEST")
        print(job)
        block = f"""
        Role {i + 1}:
        - Job Title: {job['job_title']}
        - Description: {job['description']}
        - Job Level: {job['job_level']}
        - Employment Type: {job['employment_type']}
        - Work Arrangement: {job['work_arrangement']}
        - Salary: {job['salary']['currency']} {job['salary']['min']}–{job['salary']['max']} ({job['salary']['period']})
        - Pay Schedule: {job['pay_schedule']}
        - Skills Required: {", ".join(job['skills'])}
        """.strip()

        job_blocks.append(block)

        return f"""
        Create a recruiter-grade, Facebook-ready job post using ONLY the details below.

        The content includes MULTIPLE JOB ROLES.
        Format it as a single mass-hiring or multi-role Facebook post.

        {chr(10).join(job_blocks)}

        Rules:
        - Do NOT invent missing information
        - Do NOT change meaning
        - Do NOT merge roles
        - Clearly separate each role
        - Return ONLY the final formatted job post text
        """.strip()

