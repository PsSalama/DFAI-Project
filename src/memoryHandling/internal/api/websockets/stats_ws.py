from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.memoryHandling.internal.api.websockets.websocket_manager import websocket_manager


router = APIRouter()

@router.websocket("/ws/demo")
async def demo_websocket(websocket: WebSocket):
    await websocket_manager.connect(websocket)

    try:
        while True:
            # keep connection alive safely
            await websocket.receive_text()

    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)

    except Exception:
        websocket_manager.disconnect(websocket)