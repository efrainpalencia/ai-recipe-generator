import requests
from flask import Blueprint, request, jsonify
from config import Config

recipe_routes = Blueprint("recipe_routes", __name__)


def verify_token(token):
    """Calls the Authentication Service to validate JWT tokens."""
    try:
        response = requests.post(
            f"{Config.AUTH_SERVICE_URL}/verify-token", json={"token": token})
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        return None
    return None


def fetch_ai_recipe(ingredients, preferences=""):
    """Calls the OpenAI Microservice to generate a recipe."""
    try:
        response = requests.post(
            f"{Config.OPENAI_SERVICE_URL}/generate-recipe",
            json={"ingredients": ingredients, "preferences": preferences}
        )
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        return None
    return None


@recipe_routes.route("/generate-recipe", methods=["POST"])  # ✅ Fixed route
def generate_recipe():
    """Handles user requests and fetches AI-generated recipes."""
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    user_data = verify_token(token)
    if not user_data:
        return jsonify({"error": "Invalid token!"}), 401

    data = request.json
    ingredients = data.get("ingredients", [])
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipe = fetch_ai_recipe(ingredients, preferences)
    if not recipe:
        return jsonify({"error": "Failed to generate recipe"}), 500

    return jsonify(recipe), 200
