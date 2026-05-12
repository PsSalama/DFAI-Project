from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # Default MongoDB Values
    MONGO_URI: str
    MONGO_DB_NAME: str = "dfai_db"

    # Default Redis & Celery Values
    REDIS_URI: str = "redis://localhost:6379/0"
    REDIS_RESULT_BACKEND: str = "redis://localhost:6379/1"

    # ✅ ADD THESE TWO LINES
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"  # Reads from .env
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"  # Reads from .env
    CELERY_QUEUE_NAME: str = "dfai_qu"

    # Default Celery Task Settings
    CELERY_TASK_TIME_LIMIT: int = 7200  # 2 hours max
    CELERY_TASK_SOFT_TIME_LIMIT: int = 6000  # 100 minutes soft limit
    CELERY_ACKS_LATE: bool = True

    # Default Other settings...
    DEBUG: bool = True
    SECRET_KEY: Optional[str] = None


settings = Settings()