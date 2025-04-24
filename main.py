import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Hello World API")


@app.get("/")
async def read_root():
    """Returns a simple Hello World message."""
    return {"message": "Hello World."}


@app.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    # Cloud Run injects the PORT environment variable
    # Default to 8080 for local development
    port = int(os.environ.get("PORT", 8080))
    # Listen on 0.0.0.0 to accept connections from outside the container
    uvicorn.run(app, host="0.0.0.0", port=port)
