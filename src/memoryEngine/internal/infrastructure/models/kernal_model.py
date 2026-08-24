from pydantic import BaseModel


class KernalModel(BaseModel):
    index: str
    address: str
    module: str
    symbol: str


