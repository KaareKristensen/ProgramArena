import logging

from fastapi import FastAPI

from .routers import healths, games

LOGGER = logging.getLogger(__name__)


def create_app():
    """
    Create the FASTAPI application
    Returns:
        [fastapi.FastAPI]: the main application
    """

    app = FastAPI(
        title="ProgramArena"
    )

    app.include_router(
        games.router,
        prefix="/games",
        tags=["game"],
    )

    app.include_router(
        healths.router,
        prefix="/health",
        tags=["health"],
    )

    return app
