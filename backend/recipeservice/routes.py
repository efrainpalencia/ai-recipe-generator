import openai
import json
import logging
from flask import Blueprint, request, jsonify, current_app
from config import Config

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

api = Blueprint("api", __name__)
openai.api_key = Config.OPENAI_API_KEY


def fetch_ai_recipe(ingredients, servings, cuisine, preferences=""):
    """Calls OpenAI API to generate a structured recipe response."""
    prompt = f"""
      You are a professional chef that generates well-structured JSON recipes.

      Create a professional-quality {cuisine} recipe using these ingredients: {', '.join(ingredients)}.
      You may expand upon these ingredients to craft a professional quality recipe.
      Calculate the ingredients needed for {servings} servings.
      {"The recipe should follow these dietary preferences: " +
       preferences + "." if preferences else ""}

      Respond ONLY with valid JSON. DO NOT include Markdown formatting.

      Each ingredient must include:
      - "name": Ingredient name
      - "quantity": Measurement (e.g., "2 cups", "1 tbsp")
      - "calories": Estimated calories
      - "protein": Protein content (grams)
      - "fat": Fat content (grams)
      - "carbs": Carbohydrates (grams)

      Additionally, include a **total nutrition summary** for the entire recipe.
      Use accurate nutritional information from authoritative sources such as https://www.nutrition.gov/.

      Expected JSON Output:
      {{
          "title": "Garlic Pepper Chicken Skillet",
          "cuisine": "{cuisine}",
          "servings": "{servings}",
          "prep_time": "10 minutes",
          "cook_time": "15 minutes",
          "ingredients": [
              {{
                  "name": "Chicken Breast",
                  "quantity": "2 boneless, skinless breasts",
                  "calories": 165,
                  "protein": 31,
                  "fat": 3.6,
                  "carbs": 0
              }},
              {{
                  "name": "Garlic",
                  "quantity": "4 cloves",
                  "calories": 18,
                  "protein": 0.8,
                  "fat": 0.1,
                  "carbs": 4
              }},
              {{
                  "name": "Olive Oil",
                  "quantity": "2 tablespoons",
                  "calories": 240,
                  "protein": 0,
                  "fat": 27,
                  "carbs": 0
              }}
          ],
          "instructions": [
              "Step 1: Heat olive oil in a skillet.",
              "Step 2: Add garlic and sauté until fragrant.",
              "Step 3: Add chicken and cook until golden brown."
          ],
          "total_nutrition": {{
              "calories": 423,
              "protein": 31.8,
              "fat": 30.7,
              "carbs": 4
          }}
      }}
      """

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional chef that generates well-structured JSON recipes.."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1200,
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


@api.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    """Handles user requests and fetches AI-generated recipes."""
    data = request.json
    ingredients = data.get("ingredients", [])
    servings = data.get("servings", "4")
    cuisine = data.get("cuisine", "any")
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipe_data = fetch_ai_recipe(ingredients, servings, cuisine, preferences)

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
