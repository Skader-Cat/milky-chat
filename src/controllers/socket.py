from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect
from websockets import ConnectionClosed

from service.auth import AuthManager
from service.sockets import ChatSocketManager

socket_router = APIRouter()
chat = ChatSocketManager()

@socket_router.websocket("/chat_ws")
async def websocket_endpoint(websocket: WebSocket, current_user=Depends(AuthManager.get_current_user)):
    await chat.accept_connection(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            if data["command"] == "join":
                await chat.join_room(websocket, data["room_id"], current_user)
            elif data["command"] == "leave":
                print("LEAVE", data)
                await chat.leave_room(websocket, data["room_id"])
            elif data["command"] == "message":
                await chat.broadcast_message(data, current_user)
            else:
                await chat.send_message(websocket, "Unknown message type")
    except WebSocketDisconnect:
        await chat.disconnect(websocket)
        print("DISCONNECTED BY WEBSOCKETDISCONNECT", chat.room_connections)
        for room_id in chat.room_connections:
            if websocket in chat.room_connections[room_id]:
                await chat.leave_room(websocket, room_id)
    except ConnectionClosed:
        await chat.disconnect(websocket)
        print("DISCONNECTED BY CONNECTIONCLOSED")
        for room_id in chat.room_connections:
            if websocket in chat.room_connections[room_id]:
                await chat.leave_room(websocket, room_id)
    except Exception as e:
        print(e)
        print("DISCONNECTED BY EXCEPTION")
        await chat.disconnect(websocket)
        for room_id in chat.room_connections:
            if websocket in chat.room_connections[room_id]:
                await chat.leave_room(websocket, room_id)