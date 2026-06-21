from fastapi import WebSocket
import asyncio


class WebSocketManager:
    def __init__(self):
        self.connections: list[WebSocket] = []
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        async with self.lock:
            self.connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        async with self.lock:
            if websocket in self.connections:
                self.connections.remove(websocket)

    async def broadcast(self, data: dict):
        dead = []

        async with self.lock:
            for conn in self.connections:
                try:
                    await conn.send_json(data)
                except Exception:
                    dead.append(conn)

        for conn in dead:
            await self.disconnect(conn)


websocket_manager = WebSocketManager()