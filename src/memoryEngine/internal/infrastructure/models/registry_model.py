from pydantic import BaseModel


class RegistryListModel(BaseModel):
    file_output: str
    file_full_path: str
    offset: str


class RegistryScanModel(BaseModel):
    offset: str


class RegistryKeyModel(BaseModel):
    data: str
    hive_offset: str
    key: str
    last_write_time: str
    name: str
    type: str
    volatile: str


class RegistryCertModel(BaseModel):
    certificate_id: str
    certificate_name: str
    certificate_path: str
    certificate_section: str


