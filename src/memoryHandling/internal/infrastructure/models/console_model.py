from pydantic import BaseModel


class ConsoleModel(BaseModel):
    pid: str
    process: str
    console_info: str
    property: str
    address: str
    data: str


class ConsoleCmdScanModel(BaseModel):
    pid: str
    process: str
    console_info: str
    property: str
    address: str
    data: str