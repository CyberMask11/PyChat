from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Query
from app.core.database import get_db
from app.core.security.authHandler import AuthHandler
from app.service.userService import UserService

api = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[username] = websocket

    def disconnect(self, username: str):
        self.active_connections.pop(username, None)

    async def send_message(self, message: str, username: str):
        websocket = self.active_connections.get(username)
        if websocket:
            await websocket.send_text(message)

manager = ConnectionManager()

@api.websocket('/ws')
async def ws_endpoint(ws: WebSocket,token: str = Query(...), session: Session = Depends(get_db)):
    try:
        payload = AuthHandler.decode_jwt(token)

    except Exception:
        await ws.close(code=1008)
        return
    
    user = UserService(session=session).get_user_with_id(payload["user_id"])
    user_id = str(user.id)
    displayname = user.displayname

    await manager.connect(ws, user_id)
    try:
        while True:
            data = await ws.receive_text()
            for user in manager.active_connections:
                if user != user_id:
                    await manager.send_message(f"{displayname}: {data}", user)
                
    except WebSocketDisconnect:
        manager.disconnect(user_id)
        for user in manager.active_connections:
            await manager.send_message(f"{displayname} has left the chat...", user)