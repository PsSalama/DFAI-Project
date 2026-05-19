from src.memoryHandling.infrastructure.models.activity_model import *


class ActivitySessionMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ActivitySessionModel:
        return ActivitySessionModel(
            session_id = str(raw_data.get("Session ID", "")),
            session_type = str(raw_data.get("Session Type", "")),
            process_id = str(raw_data.get("Process ID", "")),
            process = str(raw_data.get("Process", "")),
            user_name = str(raw_data.get("User Name", "")),
            create_time = str(raw_data.get("Create Time", "")),
        ).model_dump()


class ActivitySidMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ActivitySidModel:
        return ActivitySidModel(
            pid = str(raw_data.get("PID", "")),
            process = str(raw_data.get("Process", "")),
            sid = str(raw_data.get("SID", "")),
            name = str(raw_data.get("Name", "")),
        ).model_dump()


class ActivityDesktopMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ActivityDesktopModel:
        return ActivityDesktopModel(
            offset = str(raw_data.get("Offset", "")),
            window_station = str(raw_data.get("Window Station", "")),
            session = str(raw_data.get("Session", "")),
            desktop = str(raw_data.get("Desktop", "")),
            process = str(raw_data.get("Process", "")),
            pid = str(raw_data.get("PID", "")),
        ).model_dump()