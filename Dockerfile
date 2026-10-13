# Base image matching DevOps Laboratory standard
FROM python:3.11-slim

# Maintainer metadata
LABEL maintainer="Campus Event Board Team <devops@cit.edu.in>"
LABEL project="Campus Event Board"
LABEL laboratory="23IT723 - DevOps Laboratory"

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DB_DIR=/app/data \
    PORT=5000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency definition and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py /app/
COPY test_app.py /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

# Define persistent storage volume mount point
VOLUME ["/app/data"]

# Expose internal Flask service port
EXPOSE 5000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Launch application
CMD ["python", "app.py"]
