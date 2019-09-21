from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def is_healthly():
    return [{"message": "ProgramArena is up"}]
