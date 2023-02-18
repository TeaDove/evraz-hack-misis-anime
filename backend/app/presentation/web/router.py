from fastapi import APIRouter, Query, status
from fastapi.exceptions import HTTPException

from presentation.dependencies import container
from presentation.schemas import ExhausterEventsResponse
from repository.mongo_repository import SortOrders

router = APIRouter(prefix="")


@router.get("/ping")
async def get_server_status():
    return "pong"


@router.get("/events", response_model=ExhausterEventsResponse)
async def get_exhauster_events(
    exhauster_id: int = Query(..., example=1),
    page: int = Query(..., example=1),
    size: int = Query(..., example=20),
    sort_order: SortOrders = SortOrders.DESC,
):
    if page < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="page should greater than 0",
        )

    result = container.exhauster_service.get_events_by_exhauster(
        exhauster_id=exhauster_id, sort_order=sort_order, page=page, size=size
    )
    return ExhausterEventsResponse(events=list(result))
