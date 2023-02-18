from fastapi import APIRouter, Path, Query, status
from fastapi.exceptions import HTTPException

from presentation.dependencies import container
from presentation.schemas import (
    ExhausterEventsResponse,
    ExhausterResponse,
    ExhaustersResponse,
)
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


@router.get("/exhauster", response_model=ExhaustersResponse)
async def get_exhausters():
    result = container.exhauster_service.get_exhausters()
    return ExhaustersResponse(exhausters=list(result))


@router.get("/exhauster/{exhauster_id}", response_model=ExhausterResponse)
async def get_exhauster(exhauster_id: int = Path(..., example=1)):
    result = container.exhauster_service.get_exhauster(exhauster_id=exhauster_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="exhauster not found"
        )

    return ExhausterResponse(exhauster=result)
