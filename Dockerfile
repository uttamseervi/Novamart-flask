# Use a small, supported Python base
FROM python:3.11-slim

WORKDIR /app

# Install pip deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose container port (Flask default)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
