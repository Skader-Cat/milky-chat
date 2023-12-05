from fastapi import FastAPI, APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket

import controllers
import models
import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup():
    engine, conn = await models.create_db_engine(settings)
    app.state.engine = engine
    app.state.conn = conn

