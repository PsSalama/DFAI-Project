from pydantic import BaseModel
from typing import Optional

class ProcessList(BaseModel):
    pid: Optional[int] = None
    ppid: Optional[int] = None
    image_file_name: Optional[str] = None
    offset: Optional[str] = None
    threads: Optional[int] = None
    handles: Optional[str] = None
    session_id: Optional[int] = None
    wow64: Optional[bool] = None
    create_time: Optional[str] = None
    exit_time: Optional[str] = None
    file_output: Optional[str] = None

class ProcessTree(BaseModel):
    pid: Optional[int] = None
    ppid: Optional[int] = None
    image_file_name: Optional[str] = None
    offset: Optional[str] = None
    threads: Optional[int] = None
    handles: Optional[str] = None
    session_id: Optional[int] = None
    wow64: Optional[bool] = None
    create_time: Optional[str] = None
    exit_time: Optional[str] = None
    file_output: Optional[str] = None

class ProcessHidden:
    pid: int
    ppid: int
    image_file_name: str
    offset: str
    threads: int
    handles: str
    session_id: int
    wow64: bool
    create_time: str
    exit_time: str
    file_output: str

class ProcessCommandLine:
    pid:int
    process:str
    args:str

class ProcessEnvironmentVars:
    pid:int
    process:str
    block:str
    variable:str
    value:str
