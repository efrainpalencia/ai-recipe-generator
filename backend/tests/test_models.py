import pytest
from models import User, Recipe, ShoppingList, NutritionData
from bson.objectid import ObjectId

# 🟢 Test User Model


def test_user_model():
    user = User(name="John Doe", email="john@example.com",
                password_hash="hashed_password", preferences=["vegan"])

    expected_output = {
        "name": "John Doe",
        "email": "john@example.com",
        "password_hash": "hashed_password",
        "preferences": ["vegan"]
    }

    assert user.to_dict().items() >= expected_output.items()

# 🟢 Test Recipe Model


def test_recipe_model():
    recipe = Recipe(
        title="Vegan Pancakes",
        ingredients=[{"ingredient": "flour", "quantity": "1 cup"}, {
            "ingredient": "milk", "quantity": "1 cup"}],
        instructions="Mix and cook",
        created_by=ObjectId(),
        nutrition_info=ObjectId()
    )

    expected_output = {
        "title": "Vegan Pancakes",
        "ingredients": [{"ingredient": "flour", "quantity": "1 cup"}, {"ingredient": "milk", "quantity": "1 cup"}],
        "instructions": "Mix and cook"
    }

    assert recipe.to_dict()["title"] == expected_output["title"]
    assert recipe.to_dict()["ingredients"] == expected_output["ingredients"]
    assert recipe.to_dict()["instructions"] == expected_output["instructions"]

# 🟢 Test Shopping List Model


def test_shopping_list_model():
    shopping_list = ShoppingList(
        user_id=ObjectId(),
        recipe_id=ObjectId(),
        items=[{"ingredient": "flour", "quantity": "1 cup"},
               {"ingredient": "milk", "quantity": "1 cup"}]
    )

    assert isinstance(shopping_list.to_dict()["user_id"], str)
    assert isinstance(shopping_list.to_dict()["recipe_id"], str)
    assert len(shopping_list.to_dict()["items"]) == 2

# 🟢 Test Nutrition Data Model


def test_nutrition_data_model():
    nutrition = NutritionData(
        ingredient="flour",
        calories=100,
        protein=3,
        fat=0.5,
        carbs=22
    )

    expected_output = {
        "ingredient": "flour",
        "calories": 100,
        "protein": 3,
        "fat": 0.5,
        "carbs": 22
    }

    assert nutrition.to_dict().items() >= expected_output.items()
