from pydantic import BaseModel

class ProcessEnvironmentVarsModel(BaseModel):
    pid: str
    process: str
    block: str
    variable: str
    value: str