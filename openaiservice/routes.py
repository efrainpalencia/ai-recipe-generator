import openai
import json
import logging
from flask import Blueprint, request, jsonify, current_app
from config import Config

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

openai_routes = Blueprint("openai_routes", __name__)
openai.api_key = Config.OPENAI_API_KEY


def fetch_ai_recipe(ingredients, cuisine, preferences=""):
    """Calls OpenAI API to generate a structured recipe response."""
    prompt = f"""
    Create a professional-quality {cuisine} recipe using these ingredients: {', '.join(ingredients)}.
    {"The recipe should follow these dietary preferences: " +
        preferences + "." if preferences else ""}

    Ensure the response is **valid JSON**, without Markdown formatting.

    Each ingredient must include:
    - Name
    - Quantity with unit of measurement (e.g., "2 cups", "1 tbsp")
    - Calories
    - Protein (grams)
    - Fat (grams)
    - Carbohydrates (grams)

    Additionally, include a **total nutrition summary** for the entire recipe. Make sure to use
    accurate information from a trusted source such as https://www.nutrition.gov/.
    """

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are British celebrity chef and restaurateur Gordan James Ramsay that generates well-structured JSON recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1200
        )

        # Log raw AI response
        raw_text = response.choices[0].message.content.strip()
        # logging.debug(f"🔹 Raw AI Response: {raw_text}")

        # ✅ Ensure AI response is valid JSON by stripping unwanted artifacts
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace(
                "```json", "").replace("```", "").strip()

        # ✅ Convert cleaned string response to JSON
        return json.loads(raw_text)

    except json.JSONDecodeError:
        # logging.error(f"❌ JSONDecodeError - Raw Response: {raw_text}")
        return {"error": "Failed to parse the AI-generated response as JSON.", "raw_response": raw_text}

    except openai.OpenAIError as e:
        # logging.error(f"❌ OpenAI API Error: {str(e)}")
        return {"error": f"OpenAI API Error: {str(e)}"}

    except Exception as e:
        # logging.error(f"❌ Unexpected Error: {str(e)}")
        return {"error": f"Unexpected Error: {str(e)}"}


@openai_routes.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    """Handles user requests and fetches AI-generated recipes."""
    data = request.json
    ingredients = data.get("ingredients", [])
    cuisine = data.get("cuisine", "")
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipe_data = fetch_ai_recipe(ingredients, cuisine, preferences)

    if "error" in recipe_data:
        return jsonify(recipe_data), 500  # ✅ Handle API errors properly

    # ✅ Ensure expected field ordering
    ordered_recipe = {
        "title": recipe_data.get("title", "Untitled Recipe"),
        "servings": recipe_data.get("servings", "Unknown"),
        "prep_time": recipe_data.get("prep_time", "Unknown"),
        "cook_time": recipe_data.get("cook_time", "Unknown"),
        "ingredients": recipe_data.get("ingredients", []),
        "instructions": recipe_data.get("instructions", []),
        "total_nutrition": recipe_data.get("total_nutrition", [])
    }

    # ✅ Use `json.dumps()` instead of `jsonify()` to maintain order
    return current_app.response_class(
        response=json.dumps(ordered_recipe, indent=4, sort_keys=False),
        status=200,
        mimetype="application/json"
    )
