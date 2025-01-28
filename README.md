# 📌 AI Recipe Generator API Gateway

This API Gateway centralizes routing for authentication, recipe generation, and OpenAI interactions. It forwards requests to the appropriate microservices.

---

## 🚀 Getting Started

### 1️⃣ Run the Services

#### Using **Docker Compose**:

```bash
docker-compose up --build
```

Alternatively, run each service manually:

```bash
# API Gateway
cd apigateway && python api_gateway.py

# Authentication Service
cd authservice && python auth_service.py

# Recipe Service
cd recipeservice && python recipe_service.py

# OpenAI Service
cd openaiservice && python openai_service.py
```

---

## 📌 API Endpoints

### 🏷️ Authentication Service

| Method   | Endpoint            | Description                            |
| -------- | ------------------- | -------------------------------------- |
| **POST** | `/api/register`     | Registers a new user                   |
| **POST** | `/api/login`        | Logs in a user and returns a JWT token |
| **POST** | `/api/verify-token` | Validates a JWT token                  |

### 🥗 Recipe Service

| Method   | Endpoint               | Description                                                       |
| -------- | ---------------------- | ----------------------------------------------------------------- |
| **POST** | `/api/generate-recipe` | Generates a recipe based on ingredients, cuisine, and preferences |

🔹 **Request Body Example:**

```json
{
  "ingredients": ["chicken", "garlic", "onion", "pepper"],
  "cuisine": "Italian",
  "preferences": "low-carb"
}
```

🔹 **Response Example:**

```json
{
  "title": "Garlic Pepper Chicken Skillet",
  "servings": 2,
  "prep_time": "10 minutes",
  "cook_time": "15 minutes",
  "ingredients": [
    {
      "name": "Chicken Breast",
      "quantity": "2 boneless, skinless breasts",
      "calories": 165,
      "protein": 31,
      "fat": 3.6,
      "carbs": 0
    }
  ],
  "instructions": [
    "Step 1: Heat olive oil in a skillet.",
    "Step 2: Add garlic and sauté until fragrant.",
    "Step 3: Add chicken and cook until golden brown."
  ],
  "total_nutrition": {
    "calories": 423,
    "protein": 31.8,
    "fat": 30.7,
    "carbs": 4
  }
}
```

---

## 🔧 Environment Variables

Each microservice uses an `.env` file. Example `.env` configuration:

```ini
# API Gateway
AUTH_SERVICE_URL=http://auth_service:5001
RECIPE_SERVICE_URL=http://recipe_service:5002
OPENAI_SERVICE_URL=http://openai_service:5003

# Authentication Service
MONGO_URI=mongodb://localhost:27017/auth_db
JWT_SECRET=super_secret_key
AUTH_SERVICE_PORT=5001

# OpenAI Service
OPENAI_API_KEY=your_openai_api_key
```

---

## 📌 CORS Configuration

CORS has been enabled in `api_gateway.py` to allow frontend communication:

```python
from flask_cors import CORS
CORS(app)
```

---

## 🔥 Testing the API

You can test the API using **Postman** or **cURL**.

✅ **Example cURL Request:**

```bash
curl -X POST http://localhost:8080/api/generate-recipe \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer your_jwt_token" \
     -d '{"ingredients": ["chicken", "garlic", "onion", "pepper"], "cuisine": "Mexican", "preferences": "low-carb"}'
```

---

## 🚀 Next Steps

- 📌 **Frontend Integration**: Connect the API to a frontend React app.
- 📌 **Deployment**: Deploy using **Docker** + **AWS**.
- 📌 **Error Handling**: Improve validation and logging.

---

## 🎯 Contributors

Feel free to contribute by submitting a pull request or creating an issue.

---

**🔹 Happy Cooking with AI!** 🍽️ 🚀
