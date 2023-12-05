from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

import service
from dependencies import get_async_db_session
from views import UserAuth

auth = APIRouter()

@auth.get("/register", response_model=UserAuth.Register)
async def register(response: Response, user: UserAuth.Register, db=Depends(get_async_db_session)):
    return {"message": user.email}

@auth.get("/login", response_model=UserAuth.Login)
async def login(response: Response, user: UserAuth.Login, db=Depends(get_async_db_session)):
    return {"message": "Login Here"}