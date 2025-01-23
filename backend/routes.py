from flask import Blueprint, request, jsonify
from services.openai_service import generate_recipe
from services.nutrition_service import fetch_nutrition
from services.shopping_list_service import extract_ingredients

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


# In-memory storage for now (can be replaced with a database)
user_shopping_lists = {}


@api_routes.route("/generate-shopping-list", methods=["POST"])
def generate_shopping_list():
    """
    API endpoint to generate a shopping list from a recipe's ingredients.

    Request JSON:
        {
            "user_id": "12345",
            "ingredients": ["1 cup flour", "2 eggs", "1/2 cup milk"]
        }

    Returns:
        JSON response with a shopping list containing ingredient names and quantities.
    """
    data = request.json
    if not data or "ingredients" not in data or "user_id" not in data:
        return jsonify({"error": "Missing user_id or ingredients parameter"}), 400

    user_id = data["user_id"]
    shopping_list = extract_ingredients(data["ingredients"])

    # Store the generated shopping list for the user
    user_shopping_lists[user_id] = shopping_list

    return jsonify({"user_id": user_id, "shopping_list": shopping_list}), 200


@api_routes.route("/update-shopping-list", methods=["POST"])
def update_shopping_list():
    """
    API endpoint to update the shopping list after user edits.

    Request JSON:
        {
            "user_id": "12345",
            "updated_list": [
                {"ingredient": "flour", "quantity": "2 cups"},
                {"ingredient": "milk", "quantity": "1/2 cup"}
            ]
        }

    Returns:
        JSON response with the updated shopping list.
    """
    data = request.json
    if not data or "updated_list" not in data or "user_id" not in data:
        return jsonify({"error": "Missing user_id or updated_list parameter"}), 400

    user_id = data["user_id"]
    updated_list = data["updated_list"]

    user_shopping_lists[user_id] = updated_list

    return jsonify({"user_id": user_id, "shopping_list": updated_list}), 200
