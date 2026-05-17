from pydantic import BaseModel


class DllListModel(BaseModel):
    pid: str 
    process_base: str
    size: str
    name: str
    path: str
    load_count: str
    load_time: str
    file_output: str
    
    
class DllLdrmodulesModel(BaseModel):
    pid: str
    process_base: str
    in_load: str
    in_init: str
    in_mem: str
    mapped_path: str


class DllModuleModel(BaseModel):
    offset: str
    base: str
    size: str
    name: str
    path: str
    file_output: str


class DllModscanModel(BaseModel):
    offset: str
    base: str
    size: str
    name: str
    path: str
    file_output: str