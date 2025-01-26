import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# class Config:
#     API_GATEWAY_PORT = int(os.getenv("API_GATEWAY_PORT", 8080))
#     AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:5001")
#     RECIPE_SERVICE_URL = os.getenv(
#         "RECIPE_SERVICE_URL", "http://localhost:5002")
#     OPENAI_SERVICE_URL = os.getenv(
#         "OPENAI_SERVICE_URL", "http://localhost:5003")


class Config:
    # When running without Docker, use localhost
    AUTH_SERVICE_URL = "http://localhost:5001"
    RECIPE_SERVICE_URL = "http://localhost:5002"
    OPENAI_SERVICE_URL = "http://localhost:5003"
