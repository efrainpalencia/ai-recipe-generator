# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy dependencies first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the necessary port (Railway dynamically assigns ports)
EXPOSE ${PORT}

# Use Gunicorn to run the application
CMD ["gunicorn", "--bind", "[::]:${PORT-3000}", "app:app"]
