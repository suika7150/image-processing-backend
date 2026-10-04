from fastapi import FastAPI
from app.api.v1 import health
from app.api.v1 import images

app = FastAPI()

app.include_router(
    health.router,
    prefix="/api/v1"
)

app.include_router(
    images.router,
    prefix="/api/v1"
)