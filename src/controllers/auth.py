from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request

from service.auth import AuthManager

class AuthRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.post("/login")(self.login)
        self.router.post("/logout")(self.logout)

    async def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = await AuthManager.authenticate(form_data)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        access_token = AuthManager.create_access_token(data={"id": str(user.id), "email": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    async def logout(self, request: Request):
        await AuthManager.logout(request)
        return {"message": "Logged out"}