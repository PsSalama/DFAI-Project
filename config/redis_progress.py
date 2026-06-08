#config/redis_progress.py
import redis.asyncio

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=2,
    decode_responses=True
)


