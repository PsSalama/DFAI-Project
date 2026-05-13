from config.database import Database
from config.database import Redis
from fastapi import FastAPI
# from src.memoryHandling.api.memory_controller import router as memory_router
from src.memoryHandling.api.memory_controller import router as task_memory_router
from src.projectHandling.api.project_controller import router as project_router

app = FastAPI()
app.include_router(project_router)
# app.include_router(memory_router)
app.include_router(task_memory_router)

@app.on_event("startup")
async def startup():
    # If init_db is async, you MUST use await
    await Database.init_db()
    await Redis.init_redis()

@app.on_event("shutdown")
async def shutdown():
    await Database.close_db()
    await Redis.close_redis()

