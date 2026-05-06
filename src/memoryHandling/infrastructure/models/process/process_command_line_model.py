from pydantic import BaseModel

class ProcessCommandLineModel(BaseModel):
    pid: str
    process: str
    args: str