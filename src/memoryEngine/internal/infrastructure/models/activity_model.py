from pydantic import BaseModel


class ActivitySessionModel(BaseModel):
    session_id: str
    session_type: str
    process_id: str
    process: str
    user_name: str
    create_time: str


class ActivitySidModel(BaseModel):
    pid: str
    process: str
    sid: str
    name: str


class ActivityDesktopModel(BaseModel):
    offset: str
    window_station: str
    session: str
    desktop: str
    process: str
    pid: str

