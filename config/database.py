from pymongo import MongoClient
from config.settings import settings

class Database:
    client: MongoClient = None
    db = None

    @classmethod
    async def init_db(cls):
        cls.client = MongoClient(settings.MONGO_URI)
        cls.db = cls.client[settings.MONGO_DB_NAME]
        print("MongoDB connected ✔")

    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()
            print("MongoDB connection closed.")