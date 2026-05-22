from pydantic import BaseModel


class DriverModel(BaseModel):
    offset: str
    start: str
    size: str
    service_key: str
    driver_name: str
    name: str


class DriverIrpModel(BaseModel):
    offset: str
    driver_name: str
    irp: str
    address: str
    module: str
    symbol: str