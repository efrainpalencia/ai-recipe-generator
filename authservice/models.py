from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

# ✅ Initialize MongoDB Client with Railway's MONGO_URL
client = MongoClient(Config.MONGO_URL)

# ✅ Explicitly specify the database name
db_name = Config.MONGO_DB_NAME
db = client[db_name]  # ✅ Explicitly accessing the database

# ============================ MODELS ============================


class User:
    """
    Represents a user in the system.
    """

    def __init__(self, name, email, password_hash, user_id=None):
        self._id = ObjectId(user_id) if user_id else None
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def to_dict(self):
        """Converts the User object to a dictionary."""
        return {
            "_id": str(self._id) if self._id else None,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
        }


# ============================ CRUD OPERATIONS ============================

# 🟢 User Operations

def create_user(user_data):
    """Inserts a new user into the database."""
    return str(db.users.insert_one(user_data).inserted_id)  # ✅ Uses correct DB reference


def get_user_by_email(email):
    """Retrieves a user by email."""
    return db.users.find_one({"email": email})  # ✅ Uses correct DB reference
