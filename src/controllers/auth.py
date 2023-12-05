from fastapi import APIRouter
from starlette.responses import HTMLResponse

auth = APIRouter()

@auth.get("/register")
async def get():
    return {"message": "Register Here"}

@auth.get("/login")
async def login():
    return {"message": "Login Here"}