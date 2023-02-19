from datetime import datetime
from typing import Any, Dict, Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from schemas.status import ExhausterStatus


class Exhauster(BaseModel):
    exhauster_id: int
    name: str
    machine_name: str

    status: ExhausterStatus = ExhausterStatus()

    last_update: Optional[datetime] = None
    last_replacement: Optional[datetime] = None
    next_replacement_prediction: Optional[datetime] = None

    def jsonable_dict(self) -> Dict[str, Any]:
        return jsonable_encoder(self)
