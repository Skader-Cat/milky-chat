from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

import service
from dependencies import get_async_db_session
from models.schemas.user import UserFull
from views import UserAuth

auth = APIRouter()

@auth.get("/register", response_model=UserAuth.create_custom())
async def register(response: Response, user: UserAuth.Register, db=Depends(get_async_db_session)):
    return {"message": "Register Here"}

@auth.get("/login")
async def login(response: Response, user: UserAuth.Login, db=Depends(get_async_db_session)):
    return {"message": "Login Here"}