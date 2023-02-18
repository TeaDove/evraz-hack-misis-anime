from logging import _nameToLevel

import uvicorn

from presentation.web.main import create_app
from shared.settings import app_settings

uvicorn_app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "web_entrypoint:uvicorn_app",
        host="localhost",
        port=8000,
        workers=app_settings.uvicorn_workers,
        log_level=_nameToLevel["WARNING"],
    )
