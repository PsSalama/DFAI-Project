import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=2,
    decode_responses=True
)

pubsub = redis_client.pubsub()

pubsub.subscribe(
    "workflow:progress:events"
)

print("Listening...")

for message in pubsub.listen():

    if message["type"] != "message":
        continue

    print(message["data"])