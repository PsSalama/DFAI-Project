from pydantic import BaseModel

class CreateProjectInfo(BaseModel):
    project_name: str
    source_type: str
