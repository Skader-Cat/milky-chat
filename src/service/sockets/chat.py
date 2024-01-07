import datetime
from json import JSONEncoder

from sqlalchemy import DateTime

from models import schemas
from service import UserManager
from service.chat import ChatManager
from service.sockets import SocketManager


class ChatSocketManager(SocketManager):

    client_connections = {}


    @classmethod
    async def accept_connection(cls, websocket):
        await super().accept_connection(websocket)
        await super().send_system_message(websocket, "Подключение к серверу установлено")
        print("ACCEPTED CONNECTION")

    @classmethod
    async def send_message(cls, websocket, message):
        await websocket.send_json({"message": message})



    @classmethod
    async def join_room(cls, websocket, room_id, current_user):
        if room_id not in cls.room_connections:
            cls.room_connections[room_id] = set()
        cls.room_connections[room_id].add(websocket)
        print("JOIN ROOM", cls.room_connections)
        await super().send_system_message(websocket, "Вы присоединились к комнате")
        await super().broadcast_message(cls.room_connections[room_id],
                                        JSONEncoder().encode({"type": "join_message",
                                                              "username": current_user.username,
                                                              "created_at": datetime.datetime.now().strftime("%H:%M"),
                                                              "room_id": room_id}))


    @classmethod
    async def leave_room(cls, websocket, room_id):
        if room_id in cls.room_connections:
            cls.room_connections[room_id].remove(websocket)
            print("LEAVE ROOM", cls.room_connections)
            await super().send_system_message(websocket, "Вы покинули комнату")


    @classmethod
    async def broadcast_message(cls, message, current_user):
        recived_message = {}
        recived_message["text"] = message["text"]
        recived_message["user_id"] = current_user.id
        recived_message["chat_id"] = message["room_id"]
        final_message = schemas.MessageCreate(**recived_message)
        await ChatManager.add_message(recived_message, current_user, message["room_id"])
        print("BROADCAST MESSAGE", cls.room_connections)
        await super().broadcast_message(cls.room_connections[message["room_id"]],
                                        JSONEncoder().encode({"type": "message",
                                                              "user_id": str(current_user.id),
                                                              "created_at": datetime.datetime.now(),
                                                              "room_id": message["room_id"],
                                                              "message": message["text"]}))



