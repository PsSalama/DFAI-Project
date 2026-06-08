from src.memoryHandling.internal.infrastructure.pubSub.subscriber import Subscriber
from src.memoryHandling.internal.app.services.progress_service import ProgressService


subscriber = Subscriber()
progress_service = ProgressService()

async def progress_listener():
    async for event in subscriber.listen():
        await progress_service.handle_event(
            event
        )