from typing import List
from fastapi import WebSocket

class WsConnectionManager:
    active_connections: List[WebSocket]

    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocekt: WebSocket):
        self.active_connections.remove(websocekt)