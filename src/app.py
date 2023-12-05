from fastapi import FastAPI, APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket
from lifespan import main_app_lifespan

import controllers
import models
import settings

app = FastAPI(
    lifespan=main_app_lifespan,
    **settings.AppSettings.get_properties()
)

app.include_router(controllers.auth)