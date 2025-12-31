from fastapi import FastAPI

from app.routers import ai


def setup() -> FastAPI:
    app = FastAPI()
    app.include_router(ai.router)
    return app
