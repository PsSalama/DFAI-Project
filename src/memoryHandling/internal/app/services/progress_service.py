# app/services/progress_service.py
from src.memoryHandling.internal.api.websockets.websocket_manager import websocket_manager


class ProgressService:
    async def handle_event(self, event: dict) -> dict:
        await websocket_manager.broadcast(event)
        return event