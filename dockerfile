# Use Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y gcc

# Copy requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project into the container
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "first.py"]
