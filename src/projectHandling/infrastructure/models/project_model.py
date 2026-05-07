from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict


class ProjectModel(BaseModel):
    project_id: str = Field(default_factory=lambda: f"p{ObjectId().__str__()[-6:]}", alias="_id")
    project_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    source_type: list[str] = Field(default_factory=list)
    collections: list[str] = Field(default_factory=list)