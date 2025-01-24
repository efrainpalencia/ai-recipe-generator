import openai
from flask import Flask, request, jsonify
from config import Config

app = Flask(__name__)
openai.api_key = Config.OPENAI_API_KEY


@app.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    """
    Generates a structured recipe using OpenAI API.

    Expected JSON Request:
    {
        "ingredients": ["chicken", "garlic", "tomato"],
        "preferences": "low-carb, high-protein"
    }

    Returns:
    {
        "title": "Garlic Tomato Chicken",
        "ingredients": ["2 chicken breasts", "3 cloves garlic", "1 tomato"],
        "instructions": [
            "Step 1: Chop the garlic and tomato.",
            "Step 2: Sauté the garlic in olive oil.",
            "Step 3: Add the chicken and cook until golden brown.",
            "Step 4: Add chopped tomatoes and simmer."
        ]
    }
    """
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

        # Extract response
        recipe_data = response.choices[0].message.content.strip()

        # ✅ Convert string response to JSON
        return jsonify(eval(recipe_data)), 200

    except openai.OpenAIError as e:
        return jsonify({"error": f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=5005, debug=True)  # ✅ Runs OpenAI Microservice separately
