from service.base import Manager


class SocketManager(Manager):
    room_connections = {}

    @classmethod
    async def accept_connection(cls, websocket):
        await websocket.accept()

    @classmethod
    async def disconnect(cls, websocket):
        await websocket.close()

    @classmethod
    async def broadcast_message(cls, websockets, message):
        print("BROADCAST", websockets)
        for websocket in websockets:
            await websocket.send_text(message)

    @classmethod
    async def send_system_message(cls, websocket, message):
        await websocket.send_json({"system": message})