import requests
import os
from config import Config

# Base URL for Food Data Central API
FDC_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


def fetch_nutrition(ingredient):
    """
    Fetches nutrition information for a given ingredient using the Food Data Central API.

    Args:
        ingredient (str): The name of the ingredient to look up.

    Returns:
        dict: Nutritional details (calories, protein, fat, carbs) or an error message.
    """
    api_key = os.getenv("FDC_API_KEY") or Config.FDC_API_KEY
    if not api_key:
        return {"error": "Missing Food Data Central API key"}

    params = {
        "query": ingredient,
        "api_key": api_key,
        "pageSize": 1  # Only fetch the top result
    }

    try:
        response = requests.get(FDC_API_URL, params=params)
        data = response.json()

        if "foods" not in data or not data["foods"]:
            return {"error": f"No nutrition data found for {ingredient}"}

        # Extract relevant nutrition data
        food = data["foods"][0]
        nutrients = {nutrient["nutrientName"]: nutrient["value"]
                     for nutrient in food.get("foodNutrients", [])}

        return {
            "ingredient": ingredient,
            "calories": nutrients.get("Energy", 0),
            "protein": nutrients.get("Protein", 0),
            "fat": nutrients.get("Total lipid (fat)", 0),
            "carbs": nutrients.get("Carbohydrate, by difference", 0)
        }

    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
