from fastapi import FastAPI

from .routers import liveness

app = FastAPI()

app.include_router(
    liveness.router,
    prefix="/liveness",
    tags=["liveness"],
)
