import logging
from flask import Flask
from routes import openai_routes  # ✅ Importing only routes
from config import Config

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(openai_routes)  # ✅ Register routes

if __name__ == "__main__":
    print("🚀 OpenAI Service is running on port 5003")
    app.run(port=5003, debug=True)  # ✅ Runs OpenAI Microservice separately
