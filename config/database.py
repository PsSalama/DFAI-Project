# database.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import redis.asyncio as aioredis


load_dotenv()

class Database:
    client: MongoClient = None
    db = None

    @classmethod
    def init_db(cls):
        mongo_uri = os.getenv("MONGO_URL")
        mongo_db_name = os.getenv("MONGO_DB_NAME", "dfai_db")

        if not mongo_uri:
            raise ValueError("MONGO_URI not found in environment variables")

        cls.client = MongoClient(mongo_uri)
        cls.db = cls.client[mongo_db_name]
        print(f"✅ MongoDB connected to: {mongo_db_name}")

    @classmethod
    def close_db(cls):
        if cls.client:
            cls.client.close()
            print("❌ MongoDB connection closed.")


class Redis:
    client = None

    @classmethod
    def init_redis(cls):
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/2")

        cls.client = aioredis.from_url(
            redis_url,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_timeout=5
        )
        print(f"✅ Redis connected to: {redis_url}")

    @classmethod
    def close_redis(cls):
        if cls.client:
            cls.client.close()  # Note: This needs to be async
            print("❌ Redis connection closed.")