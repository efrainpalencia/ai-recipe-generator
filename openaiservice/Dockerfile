# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 5003

# Command to run the OpenAI service
CMD ["python", "openai_service.py"]
