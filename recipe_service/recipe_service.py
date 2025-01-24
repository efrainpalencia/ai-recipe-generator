import requests
from flask import Flask, request, jsonify
from config import Config  # ✅ OpenAI Microservice URL

app = Flask(__name__)
OPENAI_SERVICE_URL = Config.OPENAI_SERVICE_URL


def fetch_ai_recipe(ingredients, preferences=""):
    """Calls the OpenAI Microservice to generate a recipe."""
    response = requests.post(
        f"{OPENAI_SERVICE_URL}/generate-recipe",
        json={"ingredients": ingredients, "preferences": preferences}
    )
    return response.json() if response.status_code == 200 else None


@app.route("/generate-recipe", methods=["POST"])  # ✅ Fixed route name
def generate_recipe():
    """Handles user requests and fetches AI-generated recipes."""
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    data = request.json
    ingredients = data.get("ingredients", [])
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipe = fetch_ai_recipe(ingredients, preferences)
    if not recipe:
        return jsonify({"error": "Failed to generate recipe"}), 500

    return jsonify(recipe), 200


if __name__ == "__main__":
    print("🚀 Recipe Service is running on port 5002")
    app.run(port=5002, debug=True)  # ✅ Recipe Microservice runs separately
