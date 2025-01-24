from flask import Flask
from flask_pymongo import PyMongo
from routes import auth_routes
from models import init_db
from config import Config

# ✅ Initialize Flask App
app = Flask(__name__)

# ✅ Set MongoDB Config
app.config["MONGO_URI"] = Config.MONGO_URI

# ✅ Initialize Database
init_db(app)

# ✅ Register authentication routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
