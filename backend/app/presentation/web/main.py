from fastapi import FastAPI

from presentation.web.router import router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(router)
    return fastapi_app
