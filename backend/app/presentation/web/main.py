from fastapi import FastAPI
from starlette.exceptions import ExceptionMiddleware

from presentation.web.router import router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.add_middleware(ExceptionMiddleware, handlers=fastapi_app.exception_handlers)
    fastapi_app.include_router(router)
    return fastapi_app
