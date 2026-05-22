from typing import Optional

from pydantic import BaseModel


class ServiceModel(BaseModel):
    offset: str
    order: str
    pid: str
    start: str
    state: str
    type: str
    name: str
    display: str
    binary: str
    binary_registry: Optional[str] = None
    dll: str
