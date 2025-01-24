import requests
from flask import Flask, request, jsonify
from config import Config

app = Flask(__name__)

# Service Endpoints
AUTH_SERVICE_URL = Config.AUTH_SERVICE_URL
RECIPE_SERVICE_URL = Config.RECIPE_SERVICE_URL
OPENAI_SERVICE_URL = Config.OPENAI_SERVICE_URL
NUTRITION_SERVICE_URL = Config.NUTRITION_SERVICE_URL


def forward_request(service_url, path, method="GET", data=None, headers=None):
    """Forwards requests to the appropriate microservice."""
    url = f"{service_url}{path}"
    try:
        response = requests.request(method, url, json=data, headers=headers)
        return jsonify(response.json()), response.status_code
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


@app.route("/api/nutrition-info", methods=["GET"])
def get_nutrition_info():
    """Forwards nutrition data requests to the Nutrition Service."""
    return forward_request(NUTRITION_SERVICE_URL, "/nutrition-info", "GET", request.args, request.headers)


if __name__ == "__main__":
    print("🚀 API Gateway is running on port 8080")
    app.run(port=8080, debug=True)  # ✅ API Gateway runs on port 8080
