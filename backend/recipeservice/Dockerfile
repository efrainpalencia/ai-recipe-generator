# ✅ Use Python base image
FROM python:3.11

# ✅ Set the working directory
WORKDIR /app

# ✅ Copy files to the container
COPY . /app

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Expose port 5000
EXPOSE 5000

# ✅ Start Gunicorn with configuration
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
