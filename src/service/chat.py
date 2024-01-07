import datetime

from sqlalchemy import select

from models.schemas import ChatRoomResponse, UserResponse
from models.schemas.chat import MessageResponse
from models.tables import Chat, UserChat, Message
from service import UserManager
from service.base import Manager


class ChatManager(Manager):
    db = None

    @classmethod
    async def create_chat_room(cls, chat_room, current_user):
        chat_room_data = chat_room.model_dump()
        chat_room_data["created_at"] = datetime.datetime.now()
        chat_room_data["owner_id"] = current_user.id
        chat_users = chat_room_data["users"]
        chat_users.append(current_user.id)
        del chat_room_data["users"]
        chat_room_data["id"] = await cls.create(Chat, chat_room_data)
        print("CHAT_ID", chat_room_data["id"])
        for user in chat_users:
            user_chat = {
                "user_id": user,
                "chat_id": chat_room_data["id"],
                "created_at": datetime.datetime.now()
            }
            await cls.create(UserChat, user_chat)

    @classmethod
    async def get_chat_room(cls, chat_id):
        query = select(Chat).where(Chat.id == chat_id)
        result = await cls._execute_query_and_close(query)
        result = result.scalars().first()

        response_result = result.__dict__
        response_result["users"] = await cls.get_chat_users(chat_id)
        response_result["messages"] = await cls.get_chat_messages(chat_id)
        response_result["owner"] = await UserManager.get_user_by_id(result.owner_id)

        return ChatRoomResponse(**response_result)


    @classmethod
    async def get_chat_users(cls, chat_id):
        query = select(UserChat).where(UserChat.chat_id == chat_id)
        result = await cls._execute_query_and_close(query)
        users = []
        for user in result.scalars().all():
            users.append(await UserManager.get_user_by_id(user.user_id))

        return users

    @classmethod
    async def get_chat_messages(cls, chat_id) -> list[MessageResponse]:
        query = select(Message).where(Message.chat_id == chat_id)
        result = await cls._execute_query_and_close(query)
        messages = []
        for message in result.scalars().all():
            message.user = await UserManager.get_user_by_id(message.user_id)
            messages.append(MessageResponse(**message.__dict__))

        return messages

    @classmethod
    async def get_chat_rooms(cls, user_id):
        query = select(Chat).join(UserChat).where(UserChat.user_id == user_id)
        result = await cls._execute_query_and_close(query)
        chat_rooms = []
        for chat_room in result.scalars().all():
            chat_rooms.append(await cls.get_chat_room(chat_room.id))

        print("CHAT_ROOMS", chat_rooms)
        return chat_rooms

    @classmethod
    async def add_user_to_chat_room(cls, chat_room_id, user_id):
        user_chat = {
            "user_id": user_id,
            "chat_id": chat_room_id,
            "created_at": datetime.datetime.now()
        }
        await cls.create(UserChat, user_chat)


    @classmethod
    async def add_message(cls, message, current_user, room_id):
        message_data = {}
        message_data["text"] = message["text"]
        message_data["chat_id"] = room_id
        message_data["created_at"] = datetime.datetime.now()
        message_data["user_id"] = current_user.id
        print("СОХРАНЯЮ СООБЩЕНИЕ", message_data)
        await cls.create(Message, message_data)