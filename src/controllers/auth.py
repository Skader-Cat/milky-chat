from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

import service
from dependencies import get_async_db_session
from models.schemas import UserFull, UserSmall

auth = APIRouter()

@auth.get("/register")
async def register(response: Response, user: UserFull, response_class=UserSmall, db=Depends(get_async_db_session)):
    created_user = await service.auth.register(user, response, db)
    return created_user

@auth.get("/login")
async def login():
    return {"message": "Login Here"}