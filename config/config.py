from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # Mongo
    MONGO_URI: str
    MONGO_DB_NAME: str = "dfai_db"

    # Shared Redis
    REDIS_URL: str = "redis://localhost:6379/2"

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"
    CELERY_QUEUE_NAME: str = "dfai_qu"

    # Celery Limits
    CELERY_TASK_TIME_LIMIT: int = 7200
    CELERY_TASK_SOFT_TIME_LIMIT: int = 6000
    CELERY_ACKS_LATE: bool = True

    # App
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    SECRET_KEY: Optional[str] = None


settings = Settings()