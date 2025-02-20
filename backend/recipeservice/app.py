from flask import Flask
from flask_cors import CORS
from routes import api


app = Flask(__name__)
CORS(app, resources={
     r"/api/*": {"origins": ["ai-recipe-generator.up.railway.app"]}})

# Allow all origins or specify the frontend domain explicitly
# CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api, url_prefix="/api")  # ✅ Register routes

# Debug mode
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
