from typing import List

from pydantic import BaseModel

from schemas.event import ExhausterEvent
from schemas.exhauster import Exhauster


class ExhausterEventsResponse(BaseModel):
    events: List[ExhausterEvent]


class ExhaustersResponse(BaseModel):
    exhausters: List[Exhauster]


class ExhausterResponse(BaseModel):
    exhauster: Exhauster
