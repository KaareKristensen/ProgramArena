import logging

from fastapi import FastAPI

from .routers import healths, games, roots
from .core import settings

LOGGER = logging.getLogger(__name__)


def create_app():
    """
    Create the FASTAPI application
    Returns:
        [fastapi.FastAPI]: the main application
    """

    app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url=None,
        openapi_url="/api/v1/openapi.json",
    )

    app.include_router(
        roots.router,
        tags=["root"],
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
