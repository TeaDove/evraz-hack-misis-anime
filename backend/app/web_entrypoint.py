from logging import _nameToLevel

import uvicorn

from presentation.web.main import create_app
from shared.settings import app_settings

uvicorn_app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "web_entrypoint:uvicorn_app",
        host=app_settings.uvicorn_host,
        port=app_settings.uvicorn_port,
        workers=app_settings.uvicorn_workers,
        log_level=_nameToLevel["WARNING"],
    )
