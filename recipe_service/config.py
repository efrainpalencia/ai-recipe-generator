import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_SERVICE_URL = os.getenv(
        "OPENAI_SERVICE_URL", "http://localhost:5005")
