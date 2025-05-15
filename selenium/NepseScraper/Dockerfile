# Dockerfile

FROM python:3.13-alpine
FROM apache/airflow:3.0.0-python3.11

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (optional)
CMD ["python3", "main.py"]
