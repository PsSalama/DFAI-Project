from src.memoryEngine.internal.infrastructure.models.process_model import *


class ProcessViewMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessViewModel:
        return ProcessViewModel(
            offset=str(raw_data.get("Offset(Virtual)", "")),
            name=str(raw_data.get("Name", "")),
            pid=str(raw_data.get("PID", "")),
            pslist=str(raw_data.get("pslist", "")),
            psscan=str(raw_data.get("psscan", "")),
            thrdscan=str(raw_data.get("thrdscan", "")),
            csrss=str(raw_data.get("csrss", "")),
            exit_time=str(raw_data.get("Exit Time", "")),
        ).model_dump()


class ProcessListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessListModel:
        return ProcessListModel(
            pid=str(raw_data.get("PID", "")),
            ppid = str(raw_data.get("PPID", "")),
            image_file_name= str(raw_data.get("ImageFileName", "")),
            offset = str(raw_data.get("Offset(V)", "")),
            threads = str(raw_data.get("Threads", "")),
            handles = str(raw_data.get("Handles", "")),
            session_id = str(raw_data.get("SessionId", "")),
            wow64 = str(raw_data.get("Wow64", "")),
            create_time = str(raw_data.get("CreateTime", "")),
            exit_time = str(raw_data.get("ExitTime", "")),
            file_output = str(raw_data.get("File output", ""))
        ).model_dump()


class ProcessScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessScanModel:
        return ProcessScanModel(
            pid=str(raw_data.get("PID", "")),
            ppid=str(raw_data.get("PPID", "")),
            image_file_name=str(raw_data.get("ImageFileName", "")),
            offset=str(raw_data.get("Offset(V)", "")),
            threads=str(raw_data.get("Threads", "")),
            handles=str(raw_data.get("Handles", "")),
            session_id=str(raw_data.get("SessionId", "")),
            wow64=str(raw_data.get("Wow64", "")),
            create_time=str(raw_data.get("CreateTime", "")),
            exit_time=str(raw_data.get("ExitTime", "")),
            file_output=str(raw_data.get("File output", ""))
        ).model_dump()


class ProcessTreeMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessTreeModel:
        return ProcessTreeModel(
            pid=str(raw_data.get("PID", "")),
            ppid=str(raw_data.get("PPID", "")),
            image_file_name=str(raw_data.get("ImageFileName", "")),
            offset=str(raw_data.get("Offset(V)", "")),
            threads=str(raw_data.get("Threads", "")),
            handles=str(raw_data.get("Handles", "")),
            session_id=str(raw_data.get("SessionId", "")),
            wow64=str(raw_data.get("Wow64", "")),
            create_time=str(raw_data.get("CreateTime", "")),
            exit_time=str(raw_data.get("ExitTime", "")),
            audit=str(raw_data.get("Audit", "")),
            cmd=str(raw_data.get("Cmd", "")),
            path=str(raw_data.get("Path", ""))
        ).model_dump()
