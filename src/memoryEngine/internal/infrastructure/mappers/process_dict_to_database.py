from src.memoryEngine.internal.infrastructure.models.process_model import *


class ProcessListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessListModel:
        return ProcessListModel(
            pid=str(raw_data.get("pid", "")),
            ppid = str(raw_data.get("ppid", "")),
            image_file_name= str(raw_data.get("image_file_name", "")),
            offset = str(raw_data.get("offset", "")),
            threads = str(raw_data.get("threads", "")),
            handles = str(raw_data.get("handles", "")),
            session_id = str(raw_data.get("session_id", "")),
            wow64 = str(raw_data.get("wow64", "")),
            create_time = str(raw_data.get("create_time", "")),
            exit_time = str(raw_data.get("exit_time", "")),
            file_output = str(raw_data.get("file_output", ""))
        ).model_dump()


class ProcessXviewMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessXviewModel:
        return ProcessXviewModel(
            offset=str(raw_data.get("Offset(Virtual)", "")),
            name=str(raw_data.get("Name", "")),
            pid=str(raw_data.get("PID", "")),
            pslist=str(raw_data.get("pslist", "")),
            psscan=str(raw_data.get("psscan", "")),
            thrdscan=str(raw_data.get("thrdscan", "")),
            csrss=str(raw_data.get("csrss", "")),
            exit_time=str(raw_data.get("Exit Time", "")),
        ).model_dump()


class ProcessTreeMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessTreeModel:
        return ProcessTreeModel(
            pid=str(raw_data.get("pid", "")),
            ppid=str(raw_data.get("ppid", "")),
            image_file_name=str(raw_data.get("image_file_name", "")),
            offset=str(raw_data.get("offset", "")),
            threads=str(raw_data.get("threads", "")),
            handles=str(raw_data.get("handles", "")),
            session_id=str(raw_data.get("session_id", "")),
            wow64=str(raw_data.get("wow64", "")),
            create_time=str(raw_data.get("create_time", "")),
            exit_time=str(raw_data.get("exit_time", "")),
            file_output=str(raw_data.get("file_output", ""))
        ).model_dump()


class ProcessHiddenMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessHiddenModel:
        return ProcessHiddenModel(
            pid=str(raw_data.get("pid", "")),
            ppid=str(raw_data.get("ppid", "")),
            image_file_name=str(raw_data.get("image_file_name", "")),
            offset=str(raw_data.get("offset", "")),
            threads=str(raw_data.get("threads", "")),
            handles=str(raw_data.get("handles", "")),
            session_id=str(raw_data.get("session_id", "")),
            wow64=str(raw_data.get("wow64", "")),
            create_time=str(raw_data.get("create_time", "")),
            exit_time=str(raw_data.get("exit_time", "")),
            file_output=str(raw_data.get("file_output", ""))
        ).model_dump()


class ProcessCommandLineMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessCommandLineModel:
        return ProcessCommandLineModel(
            pid=str(raw_data.get("pid", "")),
            process=str(raw_data.get("ppid", "")),
            args=str(raw_data.get("offset", "")),
        ).model_dump()


class ProcessEnvironmentVarsMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessEnvironmentVarsModel:
        return ProcessEnvironmentVarsModel(
            pid=str(raw_data.get("pid", "")),
            process=str(raw_data.get("ppid", "")),
            block=str(raw_data.get("block", "")),
            variable=str(raw_data.get("variable", "")),
            value=str(raw_data.get("value", ""))
        ).model_dump()