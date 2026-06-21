import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import Database
from config.database import Redis
from src.memoryEngine.internal.api.controllers.memory_controller import router as memory_router
from src.memoryEngine.internal.api.controllers.project_controller import router as project_router
from src.memoryEngine.internal.api.websockets.stats_ws import router as stats_ws_router
from src.memoryEngine.internal.infrastructure.pubSub.subscriber import Subscriber
from src.memoryEngine.internal.infrastructure.pubSub.progress_listener import progress_listener


subscriber = Subscriber()

@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.init_db()
    Redis.init_redis()

    subscriber_task = asyncio.create_task(
        progress_listener()
    )

    print("Application started")
    print("Redis subscriber started")

    try:
        yield

    finally:
        subscriber_task.cancel()
        try:
            await subscriber_task
        except asyncio.CancelledError:
            pass

        Database.close_db()
        Redis.close_redis()
        print("Application stopped")

app = FastAPI(
    title="DFAI",
    lifespan=lifespan
)

app.include_router(project_router)
app.include_router(memory_router)
app.include_router(stats_ws_router)