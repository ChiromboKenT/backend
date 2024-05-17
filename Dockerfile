# Use the official lightweight Python image
FROM python:3.12.3-slim

# Install ffmpeg and dependencies in a single RUN command to reduce layers
RUN apt-get update && apt-get install -y ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]