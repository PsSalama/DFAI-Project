import redis.asyncio as redis
from config.config import settings


redis_client = redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)

__all__ = ["redis_client"]