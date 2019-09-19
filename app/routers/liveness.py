from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def liveness():
    return [{"liveness": "ok"}]
