from datetime import datetime
from pydantic import BaseModel, Field
from typing import Dict, Any


class ArtifactDocument(BaseModel):
    project_id: str
    source_type: str
    artifact_type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    class Config:
        orm_mode = True
    data: Dict[str, Any]