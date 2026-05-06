from pydantic import BaseModel

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