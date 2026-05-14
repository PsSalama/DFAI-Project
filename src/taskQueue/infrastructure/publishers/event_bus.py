from config.async_redis import async_redis_client
import json


class EventBus:
    def publish(self, channel: str, event: dict):
        async_redis_client.publish(
            channel,
            json.dumps(event)
        )
        print(f"Published event to {channel}")