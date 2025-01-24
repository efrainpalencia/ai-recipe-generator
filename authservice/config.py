import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Load variables from .env file


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET = os.getenv("JWT_SECRET")
    AUTH_SERVICE_PORT = int(os.getenv("AUTH_SERVICE_PORT", 5001))
