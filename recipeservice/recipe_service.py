from flask import Flask
from routes import recipe_routes  # Import only the routes
from config import Config

app = Flask(__name__)
app.register_blueprint(recipe_routes)  # ✅ Register routes
FLASK_DEBUG = Config.FLASK_DEBUG

if __name__ == "__main__":
    print("🚀 Recipe Service is running on port 5002")
    # ✅ Runs Recipe Microservice separately
    app.run(host="0.0.0.0", port=5002, debug={FLASK_DEBUG})
