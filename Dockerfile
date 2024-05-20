FROM python:3.10-slim

WORKDIR /app

COPY src/ ./src/
COPY data/ ./data/
COPY requirements_docker.txt .

# Install dependencies from requirements file
RUN pip install --no-cache-dir -r requirements_docker.txt

# Environment variables for the application
ENV OLLAMA_URL=http://localhost:11434 \
    PROJECT='PROJECT NAME HERE' \
    LOCATION='LOCATION HERE: eg: europe-west1' \
    BUCKET='BUCKET NAME HERE' \
    GOOGLE_CLOUD_PROJECT=PROJECT

# Copy application_default_credentials.json from:
# Windows: %APPDATA%\gcloud\application_default_credentials.json
# Linux/Mac:$HOME/.config/gcloud/application_default_credentials.json
# to root folder. (not a very good solution)
COPY application_default_credentials.json /app/gcloud-credentials.json

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gcloud-credentials.json

CMD ["python", "src/main.py"]
