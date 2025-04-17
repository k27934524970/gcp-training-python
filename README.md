# gcp-training-python

A toy application for very specific demo purposes.

## Local Prerequisites:

- Python3 installed.
- Docker installed.
- Google Cloud SDK (gcloud) installed and configured (logged into your Google Cloud account).

## Remote Prerequisites:

- A Google Cloud Project with the Cloud Run API and Artifact Registry API enabled.
- An Artifact Registry Docker repository created.

## Development

### Python Setup

Create and activate a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt -r requirements-dev.txt
```

Run the application locally:
```
uvicorn main:app --reload --port 8080
```
Once it's running you can curl against localhost:8080 and see the response

### Python Tests
To run the unit tests:
```
pytest
```

### Python Linting
This project uses `ruff` for fast linting and formatting.
```
ruff check .
```

## Docker

To build the docker image locally run:
```
docker build -t gcp-training-python .
```

To test the local image run:
```
docker run --rm -p 9090:8080 --name local-gcp-training-python gcp-training-python
```
Once it's running you can curl against localhost:9090 and see the response

### GCP

Uploading to Artifact Registry (replace the capitals vars):
```
# authenticate
gcloud auth configure-docker YOUR_REGION-docker.pkg.dev

# build your image
docker buildx build --platform linux/amd64 -t YOUR_REGION-docker.pkg.dev/GCP_PROJECT_NAME/YOUR_REPO_NAME/gcp-training-python .

# push image
docker push YOUR_REGION-docker.pkg.dev/GCP_PROJECT_NAME/YOUR_REPO_NAME/gcp-training-python
```

Deploy to Cloud Run:
```
gcloud run deploy gcp-training-python \
  --image YOUR_REGION-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/gcp-training-python:latest \
  --region YOUR_REGION \
  --allow-unauthenticated
```

Once deployed, gcloud will output the Service URL. You can access your running application at this URL.
