# AI Chef: AI Recipe Generator


![logo](https://github.com/user-attachments/assets/ddda8110-8280-4455-8f77-65a508a28dc6)


## 📌 Overview

The **AI Recipe Generator** is a full-stack application that generates professional-quality recipes based on user-inputted ingredients, cuisine type, and dietary preferences. The application consists of:

- **Backend**: A Flask-based API service using OpenAI to generate structured recipe responses.
- **Frontend**: A React (Vite + TypeScript + Tailwind CSS) UI for user interaction.
- **Deployment**: Hosted on **Railway**.

---

## 🛠 Installation Guide

### **1️⃣ Clone the Repository**

```sh
 git clone https://github.com/yourusername/ai-recipe-generator.git
 cd ai-recipe-generator
```

### **2️⃣ Set Up the Backend**

```sh
 cd backend
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 pip install -r requirements.txt
```

#### **Configure Environment Variables**

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your-openai-api-key
FLASK_ENV=production
FLASK_DEBUG=False
```

#### **Run the Backend Locally**

```sh
python app.py  # Or use `gunicorn -c gunicorn_config.py app:app` for production
```

---

### **3️⃣ Set Up the Frontend**

```sh
 cd ../frontend
 npm install  # Install dependencies
```

#### **Configure Frontend Environment Variables**

Create a `.env` file in the `frontend` directory:

```env
VITE_API_BASE_URL=<enter_your_backend_url>
```

#### **Run the Frontend Locally**

```sh
npm run dev  # Runs the frontend on localhost
```

---

## 🚀 Deployment Guide

### **1️⃣ Docker Setup (Optional for Local Development)**

```sh
docker-compose up --build
```

This will spin up both backend and frontend services.

### **2️⃣ Push Images to Docker Hub**

```sh
docker tag backend your-dockerhub-username/backend:latest
docker push your-dockerhub-username/backend:latest

docker tag frontend your-dockerhub-username/frontend:latest
docker push your-dockerhub-username/frontend:latest
```

### **3️⃣ Deploy on Railway**

- **Backend**: Deploy on **Railway**, ensuring correct environment variables.
- **Frontend**: Deploy on **Railway**, linking to the backend’s Railway domain.

---

## 📖 User Guide

### **🌟 How to Use the AI Recipe Generator**

1️⃣ **Enter Ingredients**: Type comma-separated ingredients (e.g., "chicken, garlic, onion").

2️⃣ **Select Cuisine**: Choose a cuisine (e.g., "Italian", "Mexican").

3️⃣ **Add Preferences (Optional)**: Specify dietary restrictions (e.g., "low-carb").

4️⃣ **Generate Recipe**: Click **Generate Recipe** to receive a structured response.

![input-recipe](https://github.com/user-attachments/assets/ff8c1e32-3fc6-4cf1-97a9-0c8b69904860)


5️⃣ **View Recipe**: The generated recipe includes:

- Recipe Title
- Ingredients List with Quantities & Nutritional Facts
- Step-by-Step Cooking Instructions
- Total Nutrition Summary

![recipe-results](https://github.com/user-attachments/assets/e6b16255-2b3a-4237-8e1e-41182b6e937c)


---

## 🛠 Troubleshooting

### **Common Issues & Fixes**

1️⃣ **Mixed Content Error** (Frontend Not Connecting to Backend)

- Ensure `VITE_API_BASE_URL` is set to the **correct HTTPS backend URL**.
- Update Railway domain if necessary.

2️⃣ **Backend Not Running on Railway**

- Check logs: `railway logs`
- Restart service: `railway up`

3️⃣ **Docker Issues**

- Run `docker-compose down` and rebuild with `docker-compose up --build`

---

## 📞 Support

For any issues, open an **issue** on GitHub or contact the project maintainers.

---

🚀 **Enjoy Cooking with AI!** 🍽
