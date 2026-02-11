import requests
from app.config.settings import settings


class FacebookPoster:
    def __init__(self):
        if not settings.FACEBOOK_ACCESS_TOKEN:
            raise RuntimeError("FACEBOOK_ACCESS_TOKEN not set")

        self.baseUrl = f"https://graph.facebook.com/{settings.FACEBOOK_API_VERSION}"

    def post_to_page(self, page_id: str, message: str) -> dict:
        url = f"{self.baseUrl}/{page_id}/feed"

        payload = {
            "message": message,
            "access_token": settings.FACEBOOK_ACCESS_TOKEN
        }

        response = requests.post(url, data=payload, timeout=15)

        if response.status_code != 200:
            raise RuntimeError(
                f"Facebook API error {response.status_code}: {response.text}"
            )

        return response.json()
