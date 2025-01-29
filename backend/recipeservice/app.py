from flask import Flask
from flask_cors import CORS
from routes import recipe_routes
from config import Config


app = Flask(__name__)
CORS(app)
app.register_blueprint(recipe_routes)  # ✅ Register routes
# ✅ Disable debug mode (Production)
app.config["DEBUG"] = False

if __name__ == "__main__":
    print("🚀 Recipe Service is running on port 5000")
    # ✅ Runs OpenAI Microservice separately
    from gunicorn.app.wsgiapp import run
    run()
