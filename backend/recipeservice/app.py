from flask import Flask
from flask_cors import CORS
from routes import recipe_routes
from config import Config


app = Flask(__name__)
CORS(app)
app.register_blueprint(recipe_routes)  # ✅ Register routes

# Debug mode
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)