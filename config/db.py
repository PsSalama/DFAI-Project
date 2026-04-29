import motor.motor_asyncio
from beanie import init_beanie
from .env import settings
from ..models import (  # Import all your Beanie Documents here
    MemoryDump,
    VolatilityResult,
    ForensicCase,
    ProcessArtifact,
    NetworkConnection,
    # Add more as you create them
)

async def init_db():
    """Initialize MongoDB connection and Beanie ODM"""

    # Create Motor client (async)
    client = motor.motor_asyncio.AsyncIOMotorClient(
        settings.MONGO_URI,
        # Recommended for production
        maxPoolSize=50,
        minPoolSize=10,
        connectTimeoutMS=5000,
        serverSelectionTimeoutMS=5000,
    )

    # Get database
    db = client[settings.MONGO_DB_NAME]

    # Initialize Beanie with all document models
    await init_beanie(
        database=db,
        document_models=[
            MemoryDump,
            VolatilityResult,
            ForensicCase,
            ProcessArtifact,
            NetworkConnection,
            # ... add all your models
        ],
        # Optional: recreate indexes on startup (good for dev)
        # recreate_views=True,  # if you use views later
    )

    print(f"✅ Connected to MongoDB: {settings.MONGO_DB_NAME}")
    return client