import requests
from flask import Blueprint, request, jsonify
from config import Config

nutrition_routes = Blueprint("nutrition_routes", __name__)


@nutrition_routes.route("/nutrition-info", methods=["GET"])
def get_nutrition_info():
    """Fetches nutritional information for an ingredient."""
    ingredient = request.args.get("ingredient")

    if not ingredient:
        return jsonify({"error": "Missing ingredient parameter"}), 400

    response = requests.get(f"{Config.FDC_API_URL}?query={
                            ingredient}&api_key={Config.FDC_API_KEY}")

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch nutrition data"}), 500

    return jsonify(response.json()), 200
