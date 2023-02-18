from typing import List

from pydantic import BaseModel

from schemas.exhauster import ExhausterEvent


class ExhausterEventsResponse(BaseModel):
    events: List[ExhausterEvent]
