import json
from flask import Blueprint, request, jsonify, current_app
from recipe_utils import fetch_ai_recipe  # Import from utils

recipe_routes = Blueprint("recipe_routes", __name__)


@recipe_routes.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    """Handles user requests and fetches AI-generated recipes."""
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    data = request.json
    ingredients = data.get("ingredients", [])
    cuisine = data.get("cuisine", "")
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipe = fetch_ai_recipe(ingredients, cuisine, preferences)
    if not recipe:
        return jsonify({"error": "Failed to generate recipe"}), 500

       # ✅ Use `json.dumps()` instead of `jsonify()` to maintain order
    return current_app.response_class(
        response=json.dumps(recipe, indent=4, sort_keys=False),
        status=200,
        mimetype="application/json"
    )
