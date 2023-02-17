from fastapi import APIRouter

router = APIRouter(prefix="")


@router.get("/ping")
async def get_server_status():
    return "pong"
