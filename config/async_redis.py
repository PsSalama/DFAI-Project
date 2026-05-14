import os
from dotenv import load_dotenv
import redis.asyncio as redis

load_dotenv()

async_redis_client = redis.from_url(
    os.environ.get('REDIS_URL', default="redis://localhost:6379"),
    decode_responses=True
)

# __all__ = ["redis_client"]
