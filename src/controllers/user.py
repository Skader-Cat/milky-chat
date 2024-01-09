from typing import List

from fastapi import APIRouter, Depends, HTTPException

from models import schemas
from service import UserManager
from service.auth import AuthManager
from service.chat import ChatManager

class UsersRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.post("/create")(self.create_user)
        self.router.delete("/delete")(self.delete_user)
        self.router.get("/search", response_model=List[schemas.UserResponse])(self.search_user)
        self.router.get("/me", response_model=schemas.UserResponse)(self.read_users_me)
        self.router.get("/user/{user_id}", response_model=schemas.UserResponse)(self.read_user)
        self.router.put("/update", response_model=schemas.UserResponse)(self.update_user)
        self.router.get("/list", response_model=schemas.UserListResponse)(self.read_users)
        self.router.get("/get_by_email", response_model=schemas.UserResponse)(self.get_user_by_email)
        self.router.get("/get_role", response_model=schemas.UserResponse)(self.get_user_role)
        self.router.get("/get_chat_rooms", response_model=list[schemas.ChatRoomSmallResponse])(self.get_chat_rooms)

    async def create_user(self, user: schemas.UserCreate):
        if await UserManager.get_user_by_email(user.email):
            raise HTTPException(status_code=400, detail="Такой пользователь уже существует")
        user.password = AuthManager.get_password_hash(user.password)
        await UserManager.create_user(user)
        return {"status": "User created", "access_token": AuthManager.create_access_token(user.model_dump())}

    async def delete_user(self, user_id: str):
        await UserManager.delete_user(user_id)

    async def search_user(self, query: str, page: int = 1, size: int = 10):
        return await UserManager.search_user(query, page, size)

    async def read_users_me(self, current_user: schemas.UserResponse = Depends(AuthManager.get_current_user)):
        if not current_user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return current_user

    async def read_user(self, user_id: str):
        return await UserManager.get_user_by_id(user_id)

    async def update_user(self, user: schemas.UserUpdate, current_user=Depends(AuthManager.get_current_user)):
        if not current_user:
            raise HTTPException(status_code=401, detail="Unauthorized")

        update_data = {}
        for key, value in user.model_dump().items():
            if value and key == "password":
                update_data[key] = AuthManager.get_password_hash(value)
            elif value:
                update_data[key] = value

        await UserManager.update_user(current_user.id, update_data)
        return await UserManager.get_user_by_id(current_user.id)

    async def read_users(self, page: int = 1, size: int = 10):
        users = await UserManager.get_user_list(page, size)
        total_users = await UserManager.get_total_users()
        return {"users": users, "total": total_users, "page": page, "size": size}

    async def get_user_by_email(self, email: str):
        return await UserManager.get_user_by_email(email)

    async def get_user_role(self, user_id: str):
        return await UserManager.get_user_role(user_id)

    async def get_chat_rooms(self, user_id: str):
        return await ChatManager.get_chat_rooms(user_id)
