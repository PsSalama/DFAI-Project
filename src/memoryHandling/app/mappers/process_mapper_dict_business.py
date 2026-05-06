from src.memoryHandling.app.models.process import *

class ProcessListMapperToBusinessModel:
    def to_business_model(self, raw_data: dict) -> ProcessList:
        return ProcessList(
            pid = raw_data.get("pid"),
            ppid = raw_data.get("ppid"),
            image_file_name = raw_data.get("image_file_name"),
            offset = raw_data.get("offset"),
            threads = raw_data.get("threads"),
            handles = raw_data.get("handles"),
            session_id = raw_data.get("session_id"),
            wow64 = raw_data.get("wow64"),
            create_time = raw_data.get("create_time"),
            exit_time = raw_data.get("exit_time"),
            file_output = raw_data.get("file_output")
        )

# class ProcessTreeMapperToBusinessModel:
#     def to_business_model(self, raw_data: dict) -> ProcessTree:
#         return ProcessTree(
#             pid = raw_data.get("pid"),
#             ppid = raw_data.get("ppid"),
#             image_file_name = raw_data.get("image_file_name"),
#             offset = raw_data.get("offset"),
#             threads = raw_data.get("threads"),
#             handles = raw_data.get("handles"),
#             session_id = raw_data.get("session_id"),
#             wow64 = raw_data.get("wow64"),
#             create_time = raw_data.get("create_time"),
#             exit_time = raw_data.get("exit_time"),
#             file_output = raw_data.get("file_output")
#         )


# class ProcessHiddenMapperToBusinessModel:
#     def to_business_model(self, raw_data: dict) -> ProcessHidden:
#         return ProcessHidden(
#             pid = raw_data.get("pid"),
#             ppid = raw_data.get("ppid"),
#             image_file_name = raw_data.get("image_file_name"),
#             offset = raw_data.get("offset"),
#             threads = raw_data.get("threads"),
#             handles = raw_data.get("handles"),
#             session_id = raw_data.get("session_id"),
#             wow64 = raw_data.get("wow64"),
#             create_time = raw_data.get("create_time"),
#             exit_time = raw_data.get("exit_time"),
#             file_output = raw_data.get("file_output")
#         )


# class ProcessCommandLineMapperToBusinessModel:
#     def to_business_model(self, raw_data: dict) -> ProcessCommandLine:
#         return ProcessCommandLine(
#             pid = raw_data.get("pid"),
#             process = raw_data.get("process"),
#             args = raw_data.get("args")
#         )
#
#
#
# class ProcessEnvironmentVarsMapperToDatabaseModel:
#     def to_business_model(self, raw_data: dict) -> ProcessEnvironmentVars:
#         return ProcessEnvironmentVars(
#             pid = raw_data.get("pid"),
#             process = raw_data.get("process"),
#             block = raw_data.get("block"),
#             variable = raw_data.get("variable"),
#             value = raw_data.get("value")
#         )
