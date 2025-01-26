from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import Config

# ✅ Initialize MongoDB
mongo = PyMongo()


def init_db(app):
    """
    Initializes the MongoDB database with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    app.config["MONGO_URI"] = Config.MONGO_URI  # ✅ Uses config-based URI
    mongo.init_app(app)

# ============================ MODELS ============================


class User:
    """
    Represents a user in the system.
    """

    def __init__(self, name, email, password_hash, preferences=None, user_id=None):
        self._id = ObjectId(user_id) if user_id else None
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.preferences = preferences if preferences else []

    def to_dict(self):
        """Converts the User object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "preferences": self.preferences
        }


class Recipe:
    """
    Represents a generated recipe.
    """

    def __init__(self, title, ingredients, instructions, created_by, nutrition_info=None, recipe_id=None):
        self._id = ObjectId(recipe_id) if recipe_id else None
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.created_by = ObjectId(created_by)
        self.nutrition_info = ObjectId(
            nutrition_info) if nutrition_info else None

    def to_dict(self):
        """Converts the Recipe object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "created_by": str(self.created_by),
            "nutrition_info": str(self.nutrition_info) if self.nutrition_info else None
        }


class ShoppingList:
    """
    Represents a shopping list associated with a recipe.
    """

    def __init__(self, user_id, recipe_id, items, list_id=None):
        self._id = ObjectId(list_id) if list_id else None
        self.user_id = ObjectId(user_id)
        self.recipe_id = ObjectId(recipe_id)
        # List of items {"ingredient": "flour", "quantity": "1 cup"}
        self.items = items

    def to_dict(self):
        """Converts the ShoppingList object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "user_id": str(self.user_id),
            "recipe_id": str(self.recipe_id),
            "items": self.items
        }


class NutritionData:
    """
    Represents nutritional data for an ingredient.
    """

    def __init__(self, ingredient, calories=0, protein=0, fat=0, carbs=0, nutrition_id=None):
        self._id = ObjectId(nutrition_id) if nutrition_id else None
        self.ingredient = ingredient
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def to_dict(self):
        """Converts the NutritionData object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "ingredient": self.ingredient,
            "calories": self.calories,
            "protein": self.protein,
            "fat": self.fat,
            "carbs": self.carbs
        }

# ============================ CRUD OPERATIONS ============================

# 🟢 User Operations


def create_user(user_data):
    """Inserts a new user into the database."""
    return str(mongo.db.users.insert_one(user_data).inserted_id)


def get_user_by_email(email):
    """Retrieves a user by email."""
    return mongo.db.users.find_one({"email": email})


# 🟢 Recipe Operations


def create_recipe(recipe_data):
    """Inserts a new recipe into the database."""
    return str(mongo.db.recipes.insert_one(recipe_data).inserted_id)


def get_recipe_by_id(recipe_id):
    """Retrieves a recipe by its ObjectId."""
    return mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})


# 🟢 Shopping List Operations


def create_shopping_list(list_data):
    """Inserts a new shopping list into the database."""
    return str(mongo.db.shopping_lists.insert_one(list_data).inserted_id)


def get_shopping_list_by_user(user_id):
    """Retrieves a shopping list by user ID."""
    return mongo.db.shopping_lists.find_one({"user_id": ObjectId(user_id)})


# 🟢 Nutrition Data Operations


def store_nutrition_data(nutrition_data):
    """Inserts nutrition data into the database."""
    return str(mongo.db.nutrition_data.insert_one(nutrition_data).inserted_id)


def get_nutrition_by_ingredient(ingredient):
    """Retrieves nutritional information for a given ingredient."""
    return mongo.db.nutrition_data.find_one({"ingredient": ingredient})
