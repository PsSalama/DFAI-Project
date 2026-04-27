from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
async def init_db():
    client = AsyncIOMotorClient()
