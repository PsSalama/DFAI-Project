from src.memoryHandling.infrastructure.models.process.process_list_model import ProcessListModel
from src.memoryHandling.infrastructure.models.process.process_environment_vars_model import ProcessEnvironmentVarsModel
from src.memoryHandling.infrastructure.models.process.process_tree_model import ProcessTreeModel
from src.memoryHandling.infrastructure.models.process.process_hidden_model import ProcessHiddenModel
from src.memoryHandling.infrastructure.models.process.process_command_line_model import ProcessCommandLineModel


class ProcessListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessListModel:
        return ProcessListModel(
            pid = str(raw_data.get("pid", "")),
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
        )


class ProcessTreeMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessTreeModel:
        return ProcessTreeModel(
            pid = str(raw_data.get("pid", "")),
            ppid = str(raw_data.get("ppid", "")),
            image_file_name = str(raw_data.get("image_file_name", "")),
            offset = str(raw_data.get("offset", "")),
            threads = str(raw_data.get("threads", "")),
            handles = str(raw_data.get("handles", "")),
            session_id = str(raw_data.get("session_id", "")),
            wow64 = str(raw_data.get("wow64", "")),
            create_time = str(raw_data.get("create_time", "")),
            exit_time = str(raw_data.get("exit_time", "")),
            file_output = str(raw_data.get("file_output", ""))
        )


class ProcessHiddenMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessHiddenModel:
        return ProcessHiddenModel(
            pid = str(raw_data.get("pid", "")),
            ppid = str(raw_data.get("ppid", "")),
            image_file_name = str(raw_data.get("image_file_name", "")),
            offset = str(raw_data.get("offset", "")),
            threads = str(raw_data.get("threads", "")),
            handles = str(raw_data.get("handles", "")),
            session_id = str(raw_data.get("session_id", "")),
            wow64 = str(raw_data.get("wow64", "")),
            create_time = str(raw_data.get("create_time", "")),
            exit_time = str(raw_data.get("exit_time", "")),
            file_output = str(raw_data.get("file_output", ""))
        )


class ProcessCommandLineMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessCommandLineModel:
        return ProcessCommandLineModel(
            pid = str(raw_data.get("pid","")),
            process = str(raw_data.get("ppid", "")),
            args = str(raw_data.get("offset", "")),
        )


class ProcessEnvironmentVarsMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ProcessEnvironmentVarsModel:
        return ProcessEnvironmentVarsModel(
            pid = str(raw_data.get("pid", "")),
            process = str(raw_data.get("ppid", "")),
            block = str(raw_data.get("block", "")),
            variable = str(raw_data.get("variable", "")),
            value = str(raw_data.get("value", ""))
        )