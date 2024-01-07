from typing import List

from fastapi import APIRouter, Depends, HTTPException

from models import schemas
from service import UserManager
from service.auth import AuthManager
from service.chat import ChatManager

users_router = APIRouter()


@users_router.post("/create")
async def create_user(user: schemas.UserCreate):
    if await UserManager.get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует")
    user.password = AuthManager.get_password_hash(user.password)
    await UserManager.create_user(user)
    return {"status": "User created", "access_token": AuthManager.create_access_token(user.model_dump())}

@users_router.delete("/delete")
async def delete_user(user_id: str):
    await UserManager.delete_user(user_id)

@users_router.get("/search", response_model=List[schemas.UserResponse])
async def search_user(query: str, page: int = 1, size: int = 10):
    return await UserManager.search_user(query, page, size)

@users_router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: schemas.UserResponse = Depends(AuthManager.get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return current_user

@users_router.get("/user/{user_id}", response_model=schemas.UserResponse)
async def read_user(user_id: str):
    return await UserManager.get_user_by_id(user_id)

@users_router.put("/update", response_model=schemas.UserResponse)
async def update_user(user: schemas.UserUpdate, current_user=Depends(AuthManager.get_current_user)):
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

    


@users_router.get("/list", response_model=schemas.UserListResponse)
async def read_users(page: int = 1, size: int = 10):
    users = await UserManager.get_user_list(page, size)
    total_users = await UserManager.get_total_users()
    return {"users": users, "total": total_users, "page": page, "size": size}


@users_router.get("/get_by_email", response_model=schemas.UserResponse)
async def get_user_by_email(email: str):
    return await UserManager.get_user_by_email(email)

@users_router.get("/get_role", response_model=schemas.UserResponse)
async def get_user_role(user_id: str):
    return await UserManager.get_user_role(user_id)

@users_router.get("/get_chat_rooms", response_model=list[schemas.ChatRoomSmallResponse])
async def get_chat_rooms(user_id: str):
    return await ChatManager.get_chat_rooms(user_id)