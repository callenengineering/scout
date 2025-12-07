import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import api_router

app_title = os.environ.get("APP_TITLE", "Scout")
environment = os.environ.get("ENVIRONMENT", "localhost")

title = f"{app_title}: {environment}"

app = FastAPI(title=title, description="Scout API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(api_router)