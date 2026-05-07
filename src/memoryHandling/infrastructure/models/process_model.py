from pydantic import BaseModel

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
    file_output: str


class ProcessHiddenModel(BaseModel):
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


class ProcessCommandLineModel(BaseModel):
    pid: str
    process: str
    args: str


class ProcessEnvironmentVarsModel(BaseModel):
    pid: str
    process: str
    block: str
    variable: str
    value: str