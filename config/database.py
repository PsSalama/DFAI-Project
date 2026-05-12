from pymongo import MongoClient
from config.config import settings
from redis import asyncio as aioredis


class Database:
    client: MongoClient = None
    db = None

    @classmethod
    async def init_db(cls):
        cls.client = MongoClient(settings.MONGO_URI)
        cls.db = cls.client[settings.MONGO_DB_NAME]
        print("✅ MongoDB connected ✔")

    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()
            print("❌ MongoDB connection closed.")

class Redis:
    client = None

    @classmethod
    async def init_redis(cls):
        """Initialize Redis connection"""
        try:
            cls.client = aioredis.from_url(
                settings.REDIS_URI,
                decode_responses=True,   # Automatically decode bytes to str
                socket_connect_timeout=5,
                socket_timeout=5
            )
            # Test connection
            await cls.client.ping()
            print("✅ Redis connected ✔")
        except Exception as e:
            print(f"❌ Redis connection failed: {e}")
            raise

    @classmethod
    async def close_redis(cls):
        """Close Redis connection"""
        if cls.client:
            await cls.client.close()
            print("❌ Redis connection closed.")