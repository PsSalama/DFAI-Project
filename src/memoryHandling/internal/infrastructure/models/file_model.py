from pydantic import BaseModel


class FileScanModel(BaseModel):
    offset: str
    name: str


class FileDumpModel(BaseModel):
    cache: str
    file_object: str
    file_name: str
    result: str
