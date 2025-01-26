from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import create_user, get_user_by_email, get_user_contact_info
from config import Config

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route("/register", methods=["POST"])
def register():
    """Registers a new user and hashes their password."""
    data = request.json
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if get_user_by_email(data["email"]):
        return jsonify({"error": "User already exists"}), 400

    user_data = {
        "name": data["name"],
        "email": data["email"],
        "phone_number": data["phone_number"],
        "carrier": data["carrier"],
        "password_hash": generate_password_hash(data["password"]),
    }
    user_id = create_user(user_data)

    return jsonify({"message": "User registered successfully", "user_id": str(user_id)}), 201


@auth_routes.route("/login", methods=["POST"])
def login():
    """Authenticates users and returns a JWT token."""
    data = request.json
    user = get_user_by_email(data["email"])

    if not user or not check_password_hash(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {"user_id": str(user["_id"]), "exp": datetime.datetime.utcnow(
        ) + datetime.timedelta(hours=24)},
        Config.JWT_SECRET,
        algorithm="HS256"
    )

    return jsonify({"token": token, "message": "Login successful"}), 200


@auth_routes.route("/verify-token", methods=["POST"])
def verify_token():
    """Validates JWT tokens for other microservices."""
    data = request.json
    token = data.get("token")

    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    try:
        decoded_token = jwt.decode(
            token, Config.JWT_SECRET, algorithms=["HS256"])
        return jsonify(decoded_token), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired!"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token!"}), 401


@auth_routes.route("/get-user-contact", methods=["GET"])
def get_user_contact():
    """Fetches the user's phone number and carrier for SMS notifications."""
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user_info = get_user_contact_info(user_id)
    if not user_info:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user_info), 200
