import requests
from config import Config


def fetch_ai_recipe(ingredients, cuisine, preferences=""):
    """Calls the OpenAI Microservice to generate a recipe."""
    try:
        response = requests.post(
            f"{Config.OPENAI_SERVICE_URL}/generate-recipe",
            json={"ingredients": ingredients,
                  "cuisine": cuisine, "preferences": preferences}
        )
        return response.json() if response.status_code == 200 else None
    except requests.RequestException as e:
        return None
