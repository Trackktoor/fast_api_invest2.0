import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routers import index


def create_app() -> FastAPI:
    current_path = os.path.dirname(__file__)
    static_files = os.path.join(
        current_path,
        "public/static",
    )

    app = FastAPI()
    app.mount(
        path="/static",
        app=StaticFiles(
            directory=static_files,
        ),
        name="static",
    )
    app.include_router(index.index_router)

    return app