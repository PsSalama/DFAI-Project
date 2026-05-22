from pydantic import BaseModel


class PrivilegeProcessModel(BaseModel):
    pid: str
    process: str
    value: str
    privilege: str
    attributes: str
    description: str


class PrivilegeServiceIdModel(BaseModel):
    sid: str
    service: str
    pdb_scanning_finished: str


