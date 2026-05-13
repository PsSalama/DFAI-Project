from config.redis import redis_client
import json


class EventBus:
    async def publish(self, channel: str, event: dict):
        await redis_client.publish(
            channel,
            json.dumps(event)
        )