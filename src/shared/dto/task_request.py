from typing import Any
from pydantic import BaseModel


class TaskRequest(BaseModel):
    task_name: str
    payload: dict[str, Any]

