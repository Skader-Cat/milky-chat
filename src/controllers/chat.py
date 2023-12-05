from fastapi import APIRouter
from starlette.websockets import WebSocket

chat = APIRouter()

@chat.websocket("/chat")
async def chat_init(websocket: WebSocket):
    await websocket.accept()
    return await websocket.send_json({"message": "Hello World!"})

@chat.websocket("/chat/{room_id}")
async def chat_room(websocket: WebSocket, room_id: str):
    await websocket.accept()
    return await websocket.send_json({"message": f"Hello {room_id}!"})