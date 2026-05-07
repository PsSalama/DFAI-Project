from src.memoryHandling.infrastructure.models.process_model import *
from src.memoryHandling.infrastructure.models.document_model import ArtifactDocument


class ProcessListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(project_id: str, source_type: str, raw_data: dict) -> ArtifactDocument:
        return ArtifactDocument(
            project_id = project_id,
            source_type = source_type,
            artifact_type = "process",
            data = ProcessListModel(
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
        )


class ProcessTreeMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(project_id: str, source_type: str, raw_data: dict) -> ArtifactDocument:
        return ArtifactDocument(
            project_id = project_id,
            source_type = source_type,
            artifact_type = "process",
            data = ProcessTreeModel(
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
            ).model_dump()
        )


class ProcessHiddenMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(project_id: str, source_type: str, raw_data: dict) -> ArtifactDocument:
        return ArtifactDocument(
            project_id = project_id,
            source_type = source_type,
            artifact_type = "process",
            data = ProcessHiddenModel(
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
            ).model_dump()
        )


class ProcessCommandLineMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(project_id: str, source_type: str, raw_data: dict) -> ArtifactDocument:
        return ArtifactDocument(
            project_id = project_id,
            source_type = source_type,
            artifact_type = "process",
            data = ProcessCommandLineModel(
                pid = str(raw_data.get("pid", "")),
                process = str(raw_data.get("ppid", "")),
                args = str(raw_data.get("offset", "")),
            ).model_dump()
        )


class ProcessEnvironmentVarsMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(project_id: str, source_type: str, raw_data: dict) -> ArtifactDocument:
        return ArtifactDocument(
            project_id = project_id,
            source_type = source_type,
            artifact_type = "process",
            data = ProcessEnvironmentVarsModel(
                pid=str(raw_data.get("pid", "")),
                process=str(raw_data.get("ppid", "")),
                block=str(raw_data.get("block", "")),
                variable=str(raw_data.get("variable", "")),
                value=str(raw_data.get("value", ""))
            ).model_dump()
        )