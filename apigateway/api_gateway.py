import os
import requests
import json
from flask import Flask, request, jsonify
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
FLASK_DEBUG = os.getenv("FLASK_DEBUG")

# Service Endpoints
AUTH_SERVICE_URL = Config.AUTH_SERVICE_URL
RECIPE_SERVICE_URL = Config.RECIPE_SERVICE_URL
OPENAI_SERVICE_URL = Config.OPENAI_SERVICE_URL


def forward_request(service_url, path, method="GET", data=None, headers=None):
    """Forwards requests to the appropriate microservice while preserving JSON order."""
    url = f"{service_url}{path}"
    try:
        response = requests.request(method, url, json=data, headers=headers)
        response_data = response.json()

        # ✅ Preserve JSON order
        ordered_response = json.dumps(response_data, indent=4, sort_keys=False)
        return app.response_class(response=ordered_response, status=response.status_code, mimetype="application/json")

    except requests.RequestException as e:
        return jsonify({"error": f"Service Unavailable: {str(e)}"}), 503


@app.route("/api/register", methods=["POST"])
def register():
    """Forwards user registration requests to the Authentication Service."""
    return forward_request(AUTH_SERVICE_URL, "/register", "POST", request.json)


@app.route("/api/login", methods=["POST"])
def login():
    """Forwards login requests to the Authentication Service."""
    return forward_request(AUTH_SERVICE_URL, "/login", "POST", request.json)


@app.route("/api/generate-recipe", methods=["POST"])
def generate_recipe():
    """Verifies JWT, then forwards recipe requests to the Recipe Service."""
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    token_value = token.split("Bearer ")[-1]  # Extract the actual token

    # ✅ Verify JWT via Authentication Service
    auth_response = requests.post(
        f"{AUTH_SERVICE_URL}/verify-token", json={"token": token_value}
    )

    if auth_response.status_code != 200:
        return jsonify({"error": "Invalid token!"}), 401

    # ✅ Forward request to the correct endpoint in the Recipe Service
    return forward_request(RECIPE_SERVICE_URL, "/generate-recipe", "POST", request.json, request.headers)


if __name__ == "__main__":
    print("🚀 API Gateway is running on port 8080")
    # ✅ API Gateway runs on port 8080
    app.run(host="0.0.0.0", port=8080, debug={FLASK_DEBUG})
