from config.database import Database
from fastapi import FastAPI
from src.memoryHandling.api.memory_controller import router as memory_router
from src.projectHandling.api.project_controller import router as project_router

app = FastAPI()
app.include_router(project_router)
app.include_router(memory_router)

@app.on_event("startup")
async def startup():
    # If init_db is async, you MUST use await
    await Database.init_db()

@app.on_event("shutdown")
async def shutdown():
    await Database.close_db()