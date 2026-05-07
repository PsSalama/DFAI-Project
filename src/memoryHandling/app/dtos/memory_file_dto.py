from pydantic import BaseModel

class MemoryFileDto(BaseModel):
    file_path: str
    project_id: str
    source_type: str
