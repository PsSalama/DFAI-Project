from pydantic import BaseModel

class ProcessViewModel(BaseModel):
    offset: str
    name: str
    pid: str
    pslist: str
    psscan: str
    thrdscan: str
    csrss: str
    exit_time: str


class ProcessListModel(BaseModel):
    pid: str
    ppid: str
    image_file_name: str
    offset: str
    threads: str
    handles: str
    session_id: str
    wow64: str
    create_time: str
    exit_time: str
    file_output: str

class ProcessScanModel(BaseModel):
    pid: str
    ppid: str
    image_file_name: str
    offset: str
    threads: str
    handles: str
    session_id: str
    wow64: str
    create_time: str
    exit_time: str
    file_output: str


class ProcessTreeModel(BaseModel):
    pid: str
    ppid: str
    image_file_name: str
    offset: str
    threads: str
    handles: str
    session_id: str
    wow64: str
    create_time: str
    exit_time: str
    audit: str
    cmd: str
    path: str
