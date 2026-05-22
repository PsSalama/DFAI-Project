from config.database import Database
from config.database import Redis
from fastapi import FastAPI
from src.memoryHandling.internal.api.memory_controller import router as task_memory_router
from src.projectHandling.api.project_controller import router as project_router

app = FastAPI()
app.include_router(project_router)
# app.include_router(memory_router)
app.include_router(task_memory_router)

@app.on_event("startup")
async def startup():
    # If init_db is async, you MUST use await
    Database.init_db()
    Redis.init_redis()

@app.on_event("shutdown")
async def shutdown():
    Database.close_db()
    Redis.close_redis()

