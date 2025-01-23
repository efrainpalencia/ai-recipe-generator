import openai
import os
from config import Config

# Ensure OpenAI API Key is set
openai.api_key = Config.OPENAI_API_KEY


def generate_recipe(ingredients, preferences=None):
    """
    Generates a recipe using OpenAI API.

    Args:
        ingredients (list): List of ingredients provided by the user.
        preferences (str, optional): Dietary preferences (e.g., vegan, gluten-free).

    Returns:
        dict: Recipe with title, ingredients, and instructions.
    """

    prompt = f"Create a unique recipe using these ingredients: {
        ', '.join(ingredients)}."

    if preferences:
        prompt += f" The recipe should follow these dietary preferences: {
            preferences}."

    prompt += " Provide a structured response with a title, ingredients, and step-by-step instructions."

    try:
        # New API Structure (OpenAI v1.60.0)
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system",
                    "content": "You are an AI chef that creates detailed recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        # Extract structured response
        recipe_text = response.choices[0].message.content.strip().split("\n")

        return {
            "recipe": recipe_text[0],  # First line as recipe title
            "ingredients": ingredients,  # Return the given ingredients
            "instructions": recipe_text[1:]  # Remaining lines as steps
        }

    except openai.OpenAIError as e:
        return {"error": f"OpenAI API Error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected Error: {str(e)}"}
