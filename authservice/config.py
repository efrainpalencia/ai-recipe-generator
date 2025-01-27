import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URL = os.getenv("MONGO_URL")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "auth_db")
    JWT_SECRET = os.getenv("JWT_SECRET")
    AUTH_SERVICE_PORT = int(os.getenv("AUTH_SERVICE_PORT", 5001))
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
