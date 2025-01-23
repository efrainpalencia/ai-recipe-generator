from flask import Blueprint, request, jsonify
from services.openai_service import generate_recipe
from services.nutrition_service import fetch_nutrition

api_routes = Blueprint("api_routes", __name__)


@api_routes.route("/generate-recipe", methods=["POST"])
def generate_recipe_api():
    """API endpoint to generate a recipe based on user-provided ingredients."""
    data = request.json
    if not data or "ingredients" not in data:
        return jsonify({"error": "Missing ingredients"}), 400

    recipe = generate_recipe(data.get("ingredients"), data.get("preferences"))
    return jsonify(recipe), 200


@api_routes.route("/nutrition-info", methods=["GET"])
def get_nutrition_info():
    """
    API endpoint to fetch nutrition details for an ingredient.

    Request Params:
        - ingredient (str): The ingredient to look up.

    Returns:
        JSON response containing nutrition details or an error message.
    """
    ingredient = request.args.get("ingredient")

    if not ingredient:
        return jsonify({"error": "Missing ingredient parameter"}), 400

    nutrition_data = fetch_nutrition(ingredient)
    return jsonify(nutrition_data)
