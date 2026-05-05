from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from config import settings
from models.process import Process


class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    async def init_db(cls):
        # Create Mongo client
        cls.client = AsyncIOMotorClient(settings.MONGO_URI)

        # Select database
        db = cls.client[settings.MONGO_DB_NAME]

        # Initialize Beanie with document models
        await init_beanie(
            database=db,
            document_models=[
                Process
            ]
        )

        print("MongoDB connected and Beanie initialized ✔")

    @classmethod
    def close_db(cls):
        if cls.client:
            cls.client.close()