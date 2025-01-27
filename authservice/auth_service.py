from flask import Flask
from pymongo import MongoClient
from routes import auth_routes
from config import Config

# ✅ Initialize Flask App
app = Flask(__name__)

# ✅ Initialize MongoDB Client with Database Name
client = MongoClient(Config.MONGO_URL)
db = client[Config.MONGO_DB_NAME]  # ✅ Explicitly define the database

# ✅ Register authentication routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
