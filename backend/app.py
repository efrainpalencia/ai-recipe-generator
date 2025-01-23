from flask import Flask
from flask_cors import CORS
from routes import api_routes
from models import init_db

app = Flask(__name__)
CORS(app)
init_db(app)

# Load Routes
app.register_blueprint(api_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
