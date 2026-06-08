import asyncio
import json
import redis.asyncio as redis


class Subscriber:
    def __init__(self):
        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            db=2,
            decode_responses=True
        )


    async def listen(self):
        pubsub = self.redis.pubsub()
        await pubsub.subscribe(
            "workflow:progress:events"
        )

        while True:
            message = await pubsub.get_message(
                ignore_subscribe_messages=True
            )
            if message:

                yield json.loads(
                    message["data"]
                )
            await asyncio.sleep(0.1)