import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_SERVICE_PORT = int(os.getenv("OPENAI_SERVICE_PORT", 5005))
