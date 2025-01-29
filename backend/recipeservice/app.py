from flask import Flask
from flask_cors import CORS
from routes import recipe_routes
from config import Config


app = Flask(__name__)
CORS(app)
app.register_blueprint(recipe_routes)  # ✅ Register routes
FLASK_DEBUG = Config.FLASK_DEBUG

if __name__ == "__main__":
    print("🚀 Recipe Service is running on port 5000")
    # ✅ Runs OpenAI Microservice separately
    app.run(host="0.0.0.0", port=5000, debug={FLASK_DEBUG})
