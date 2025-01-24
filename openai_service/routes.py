import openai
from flask import Blueprint, request, jsonify
from config import Config

openai_routes = Blueprint("openai_routes", __name__)
openai.api_key = Config.OPENAI_API_KEY


@openai_routes.route("/generate-recipe", methods=["POST"])
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

    Format the response in JSON with:
    - "title": Recipe title.
    - "ingredients": List of ingredients with measurements.
    - "instructions": Step-by-step preparation instructions.
    """

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional chef who generates high-quality recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        recipe_data = response.choices[0].message.content.strip()
        return jsonify(eval(recipe_data)), 200

    except openai.OpenAIError as e:
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500
