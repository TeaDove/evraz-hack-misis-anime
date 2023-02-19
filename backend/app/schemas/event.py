from datetime import datetime
from typing import Any, Dict, Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from schemas.status import ExhausterStatus


class ExhausterEvent(BaseModel):
    created_at: Optional[datetime] = None

    exhauster_id: int

    status: ExhausterStatus = ExhausterStatus()

    def jsonable_dict(self) -> Dict[str, Any]:
        return jsonable_encoder(self)
