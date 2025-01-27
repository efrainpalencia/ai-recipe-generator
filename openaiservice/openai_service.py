from flask import Flask
from routes import openai_routes  # ✅ Importing only routes
from config import Config


app = Flask(__name__)
app.register_blueprint(openai_routes)  # ✅ Register routes
FLASK_DEBUG = Config.FLASK_DEBUG

if __name__ == "__main__":
    print("🚀 OpenAI Service is running on port 5003")
    # ✅ Runs OpenAI Microservice separately
    app.run(host="0.0.0.0", port=5003, debug={FLASK_DEBUG})
