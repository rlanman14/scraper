# Dockerfile

# Use the official Python slim image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ /app/

# Expose the Flask port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
