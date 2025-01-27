# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 8080

# Command to run the application
CMD ["python", "api_gateway.py"]
