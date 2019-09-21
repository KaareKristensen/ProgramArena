import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


games = {}


class Game(BaseModel):
    height: int
    width: int
    game_name: str


@router.get("/")
async def get_games():
    return {"games": games}


@router.get("/{game_id}")
async def get_game(game_id: str):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"game": games[game_id]}


@router.post("/", status_code=201)
async def create_game(game: Game):
    game_id = str(uuid.uuid4())
    games[game_id] = game
    return {"game": games[game_id]}
