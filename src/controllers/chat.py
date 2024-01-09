from fastapi import APIRouter, Depends, HTTPException

from models import schemas
from service.auth import AuthManager
from service.chat import ChatManager

class ChatRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.post("/create")(self.create_chat_room)
        self.router.get("/get_chat_room", response_model=schemas.ChatRoomResponse)(self.get_chat_room)
        self.router.get("/get_chat_room_users", response_model=list[schemas.UserResponse])(self.get_chat_room_users)
        self.router.post("/add_user")(self.add_user_to_chat_room)
        self.router.get("/remove_user")(self.remove_user_from_chat_room)
        self.router.get("/get_chat_room_messages", response_model=list[schemas.MessageResponse])(self.get_chat_room_messages)

    async def create_chat_room(self, chat_room: schemas.ChatRoomCreate, current_user=Depends(AuthManager.get_current_user)):
        await ChatManager.create_chat_room(chat_room, current_user)
        return {"status": "Chat room created"}

    async def get_chat_room(self, chat_room_id: str):
        return await ChatManager.get_chat_room(chat_room_id)

    async def get_chat_room_users(self, chat_room_id: str):
        return await ChatManager.get_chat_users(chat_room_id)

    async def add_user_to_chat_room(self, chat_room_id: str, user_id: str, current_user=Depends(AuthManager.get_current_user)):
        if not current_user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        chat = await ChatManager.get_chat_room(chat_room_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")

        await ChatManager.add_user_to_chat_room(chat_room_id, user_id)

        return {"status": "User added"}

    async def remove_user_from_chat_room(self, chat_room_id: str, user_id: str, current_user=Depends(AuthManager.get_current_user)):
        if not current_user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        chat = await ChatManager.get_chat_room(chat_room_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")

        await ChatManager.remove_user_from_chat_room(chat_room_id, user_id)

        return {"status": "User removed"}

    async def get_chat_room_messages(self, chat_room_id: str):
        return await ChatManager.get_chat_messages(chat_room_id)