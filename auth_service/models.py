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

    def __init__(self, name, email, password_hash, phone_number, carrier, user_id=None):
        self._id = ObjectId(user_id) if user_id else None
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.phone_number = phone_number
        self.carrier = carrier

    def to_dict(self):
        """Converts the User object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "phone_number": self.phone_number,
            "carrier": self.carrier
        }


# ============================ CRUD OPERATIONS ============================

# 🟢 User Operations


def create_user(user_data):
    """Inserts a new user into the database."""
    return str(mongo.db.users.insert_one(user_data).inserted_id)


def get_user_by_email(email):
    """Retrieves a user by email."""
    return mongo.db.users.find_one({"email": email})


def get_user_contact_info(user_id):
    """Retrieves a user's phone number and carrier based on user ID."""
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)}, {
                                   "phone_number": 1, "carrier": 1})
    return user if user else None
