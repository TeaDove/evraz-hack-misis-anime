from datetime import datetime
from typing import Tuple


class AppService:
    def get_time() -> Tuple[datetime, int]:
        ...
