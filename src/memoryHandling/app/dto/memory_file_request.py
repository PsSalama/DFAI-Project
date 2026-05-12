from pydantic import BaseModel

class MemoryFileRequest(BaseModel):
    file_path: str
    project_id: str
    source_type: str
