import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_SERVICE_PORT = int(os.getenv("OPENAI_SERVICE_PORT", 5003))
