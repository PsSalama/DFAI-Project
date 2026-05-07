from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic import BaseModel, Field, ConfigDict


class ProjectModel(BaseModel):
    project_id: str = Field(default_factory=lambda: f"p{ObjectId().__str__()[-6:]}", alias="_id")
    project_name: str
    source_type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    collections: list[str] = Field(default_factory=list)