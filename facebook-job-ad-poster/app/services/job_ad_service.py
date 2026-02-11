from app.agents.job_ad_writer import JobFormatterAgent
from app.tools.facebook_poster import FacebookPoster


class FacebookJobAdService:
    def __init__(self):
        self.formatter = JobFormatterAgent()
        self.poster = FacebookPoster()

    def create_and_post(self, page_id: str, job_data: list[dict]) -> dict:
        # job_data is already canonical (n8n-style)
        formatted_post = self.formatter.format(job_data)

        response = self.poster.post_to_page(
            page_id=page_id,
            message=formatted_post
        )

        return {
            "ad_text": formatted_post,
            "facebook_response": response
        }
