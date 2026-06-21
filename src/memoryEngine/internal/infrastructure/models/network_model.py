from pydantic import BaseModel


class NetworkScanModel(BaseModel):
    offset: str
    proto: str
    local_addr: str
    local_port: str
    foreign_addr: str
    foreign_port: str
    state: str
    pid: str
    owner: str
    created: str


class NetworkStatModel(BaseModel):
    offset: str
    proto: str
    local_addr: str
    local_port: str
    foreign_addr: str
    foreign_port: str
    state: str
    pid: str
    owner: str
    created: str