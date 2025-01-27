import os
from dotenv import load_dotenv, find_dotenv

# ✅ Load environment variables from .env if available
load_dotenv(find_dotenv())


class Config:
    # ✅ API Gateway
    API_GATEWAY_PORT = int(os.getenv("API_GATEWAY_PORT", 8080))
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:5001")
    RECIPE_SERVICE_URL = os.getenv(
        "RECIPE_SERVICE_URL", "http://localhost:5002")
    OPENAI_SERVICE_URL = os.getenv(
        "OPENAI_SERVICE_URL", "http://localhost:5003")

    # ✅ Authentication & Security
    JWT_SECRET = os.getenv("JWT_SECRET", "super_secret_jwt_key")

    # ✅ Database (MongoDB)
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/auth_db")

    # ✅ OpenAI API Key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
