import re

# List of common measurement units
MEASUREMENT_UNITS = [
    "cup", "cups", "tbsp", "tsp", "teaspoon", "teaspoons", "tablespoon", "tablespoons",
    "oz", "ounce", "ounces", "lb", "lbs", "pound", "pounds", "g", "gram", "grams",
    "kg", "kilogram", "kilograms", "ml", "milliliter", "milliliters", "l", "liter", "liters"
]


def extract_ingredients(recipe_ingredients):
    """
    Extracts ingredient names and their quantities from a recipe.

    Args:
        recipe_ingredients (list): A list of raw ingredient strings from the recipe.

    Returns:
        list: A structured shopping list with ingredient names and quantities.
    """
    shopping_list = []

    for ingredient in recipe_ingredients:
        # Improved regex: Captures both numeric-only and unit-based quantities
        match = re.match(
            r"^([\d/.\s]+(?:{}|\b))\s*(.*)$".format("|".join(MEASUREMENT_UNITS)), ingredient.strip())

        if match:
            quantity = match.group(1).strip()
            ingredient_name = match.group(2).strip().lower()
        else:
            # New fix: Handle numeric-only quantities (e.g., "2 eggs")
            match_numeric = re.match(r"^(\d+)\s*(.*)$", ingredient.strip())
            if match_numeric:
                quantity = match_numeric.group(1)
                ingredient_name = match_numeric.group(2).strip().lower()
            else:
                quantity = "to taste"
                ingredient_name = ingredient.strip().lower()

        # Debugging
        print(
            f"DEBUG: Extracted - Ingredient: {ingredient_name}, Quantity: {quantity}")

        if ingredient_name and not any(item["ingredient"] == ingredient_name for item in shopping_list):
            shopping_list.append(
                {"ingredient": ingredient_name, "quantity": quantity})

    return shopping_list
