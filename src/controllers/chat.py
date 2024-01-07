from fastapi import APIRouter, Depends, HTTPException

from models import schemas
from service.auth import AuthManager
from service.chat import ChatManager

chat_router = APIRouter()

@chat_router.post("/create")
async def create_chat_room(chat_room: schemas.ChatRoomCreate, current_user = Depends(AuthManager.get_current_user)):
    await ChatManager.create_chat_room(chat_room, current_user)
    return {"status": "Chat room created"}

@chat_router.get("/get_chat_room", response_model=schemas.ChatRoomResponse)
async def get_chat_room(chat_room_id: str):
    return await ChatManager.get_chat_room(chat_room_id)

@chat_router.get("/get_chat_room_users", response_model=list[schemas.UserResponse])
async def get_chat_room_users(chat_room_id: str):
    return await ChatManager.get_chat_users(chat_room_id)

@chat_router.get("/add_user")
async def add_user_to_chat_room(chat_room_id: str, user_id: str, current_user = Depends(AuthManager.get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    chat = await ChatManager.get_chat_room(chat_room_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    await ChatManager.add_user_to_chat_room(chat_room_id, user_id)

    return {"status": "User added"}

@chat_router.get("/get_chat_room_messages", response_model=list[schemas.MessageResponse])
async def get_chat_room_messages(chat_room_id: str):
    return await ChatManager.get_chat_messages(chat_room_id)
