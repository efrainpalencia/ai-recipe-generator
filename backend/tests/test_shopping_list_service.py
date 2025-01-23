import pytest
from services.shopping_list_service import extract_ingredients


def test_extract_ingredients():
    """
    Test extracting ingredients with quantities from a recipe.
    """
    recipe_ingredients = [
        "1 cup flour",
        "2 eggs",
        "1/2 cup milk",
        "1 onion",
        "1 tbsp salt"
    ]

    expected_output = [
        {"ingredient": "flour", "quantity": "1 cup"},
        {"ingredient": "eggs", "quantity": "2"},
        {"ingredient": "milk", "quantity": "1/2 cup"},
        {"ingredient": "onion", "quantity": "1"},
        {"ingredient": "salt", "quantity": "1 tbsp"}
    ]

    result = extract_ingredients(recipe_ingredients)

    # Convert lists to sets to ignore order differences
    assert set(tuple(sorted(d.items())) for d in result) == set(
        tuple(sorted(d.items())) for d in expected_output)
