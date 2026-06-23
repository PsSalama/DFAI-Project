from pydantic import BaseModel


class HandleModel(BaseModel):
    pid: str
    process: str
    offset: str
    handle_value: str
    type: str
    granted_access: str
    name: str
