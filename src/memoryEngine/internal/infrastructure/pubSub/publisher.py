import json
from config.redis_progress import redis_client


class Publisher:
    CHANNEL = "workflow:progress:events"
    def publish_progress(
        self,
        payload: dict
    ):

        redis_client.publish(
            self.CHANNEL,
            json.dumps(payload)
        )