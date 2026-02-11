import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
  OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
  FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
  FACEBOOK_API_VERSION = os.getenv("FACEBOOK_API_VERSION", "v19.0")
  #EAAT1oNMYtCMBQsKaPS0gIDcYZCnLUiyXcZAxP9AlzorZCqljwfTRf0iqskObUxbwiAA9ZAaTbZCoZAvzCt85B2y2Ob9hGfw24qI7ZBlRNnETLZCBZAO5ZCfe3aTxmNgEVooRLA7RwpZBI2YkqwQe6o3Ki9trighSc0wym6g9kX8TL4J8Bo8ZBIJzx9e8ZC0ZCloSgy

settings = Settings()