from flask import Flask
from routes import recipe_routes  # Import only the routes

app = Flask(__name__)
app.register_blueprint(recipe_routes)  # ✅ Register routes

if __name__ == "__main__":
    print("🚀 Recipe Service is running on port 5002")
    app.run(port=5002, debug=True)  # ✅ Runs Recipe Microservice separately
