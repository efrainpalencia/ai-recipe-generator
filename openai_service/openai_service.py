import openai
import json
import logging
from flask import Flask, request, jsonify
from config import Config

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
openai.api_key = Config.OPENAI_API_KEY


@app.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    """Handles AI-powered recipe generation."""
    data = request.json
    ingredients = data.get("ingredients", [])
    preferences = data.get("preferences", "")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    prompt = f"""
    Create a professional-quality recipe using these ingredients: {', '.join(ingredients)}.
    {f"The recipe should follow these dietary preferences: {
        preferences}." if preferences else ""}

    Ensure the response is valid JSON, without Markdown formatting.

    Expected JSON Output:
    {{
        "title": "Garlic Pepper Chicken Skillet",
        "servings": 2,
        "prep_time": "10 minutes",
        "cook_time": "15 minutes",
        "ingredients": [
            "2 boneless, skinless chicken breasts",
            "4 cloves garlic, minced",
            "1 onion, sliced"
        ],
        "instructions": [
            "Step 1: Heat olive oil in a skillet.",
            "Step 2: Add garlic and sauté until fragrant.",
            "Step 3: Add chicken and cook until golden brown."
        ]
    }}
    """

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI chef that generates well-structured JSON recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        # Log raw AI response
        raw_text = response.choices[0].message.content.strip()
        logging.debug(f"🔹 Raw AI Response: {raw_text}")

        # ✅ Ensure AI response is valid JSON by stripping unwanted artifacts
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace(
                "```json", "").replace("```", "").strip()

        # ✅ Convert cleaned string response to a Python dictionary
        parsed_data = json.loads(raw_text)

        # ✅ Create a new dictionary with explicit order
        ordered_recipe = {
            "title": parsed_data.get("title", "Untitled Recipe"),
            "servings": parsed_data.get("servings", "Unknown"),
            "prep_time": parsed_data.get("prep_time", "Unknown"),
            "cook_time": parsed_data.get("cook_time", "Unknown"),
            "ingredients": parsed_data.get("ingredients", []),
            "instructions": parsed_data.get("instructions", [])
        }

        # ✅ Use `json.dumps()` instead of `jsonify()` to maintain order
        return app.response_class(
            response=json.dumps(ordered_recipe, indent=4, sort_keys=False),
            status=200,
            mimetype="application/json"
        )

    except json.JSONDecodeError:
        logging.error(f"❌ JSONDecodeError - Raw Response: {raw_text}")
        return jsonify({"error": "Failed to parse the AI-generated response as JSON.", "raw_response": raw_text}), 500

    except openai.OpenAIError as e:
        logging.error(f"❌ OpenAI API Error: {str(e)}")
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500

    except Exception as e:
        logging.error(f"❌ Unexpected Error: {str(e)}")
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=5005, debug=True)  # ✅ Runs OpenAI Microservice separately
