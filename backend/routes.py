from flask import Blueprint, request, jsonify
from services.openai_service import generate_recipe

api_routes = Blueprint("api_routes", __name__)


@api_routes.route("/generate-recipe", methods=["POST"])
def generate_recipe_api():
    data = request.json
    recipe = generate_recipe(data.get("ingredients"), data.get("preferences"))
    return jsonify(recipe)
