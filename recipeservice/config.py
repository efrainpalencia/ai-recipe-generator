import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    RECIPE_SERVICE_URL = os.getenv("RECIPE_SERVICE_URL")
    OPENAI_SERVICE_URL = os.getenv("OPENAI_SERVICE_URL")
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
