import os
from flask import Flask
from pymongo import MongoClient
from routes import auth_routes
from config import Config

# ✅ Initialize Flask App
app = Flask(__name__)
FLASK_DEBUG = os.getenv("FLASK_DEBUG")

# ✅ Initialize MongoDB Client with Database Name
client = MongoClient(Config.MONGO_URL)
db = client[Config.MONGO_DB_NAME]  # ✅ Explicitly define the database

# ✅ Register authentication routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug={FLASK_DEBUG})
