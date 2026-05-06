from src.memoryHandling.app.models.process import *


class ProcessListMapperToDict:
    def to_dict(self, process_list: ProcessList) -> dict:
        return {
            "pid": process_list.pid,
            "ppid": process_list.ppid,
            "image_file_name": process_list.image_file_name,
            "offset": process_list.offset,
            "threads": process_list.threads,
            "handles": process_list.handles,
            "session_id": process_list.session_id,
            "wow64": process_list.wow64,
            "create_time": process_list.create_time,
            "exit_time": process_list.exit_time,
            "file_output": process_list.file_output,
        }

class ProcessTreeMapperToDict:
    def to_dict(self, process_tree: ProcessTree) -> dict:
        return {
            "pid": process_tree.pid,
            "ppid": process_tree.ppid,
            "image_file_name": process_tree.image_file_name,
            "offset": process_tree.offset,
            "threads": process_tree.threads,
            "handles": process_tree.handles,
            "session_id": process_tree.session_id,
            "wow64": process_tree.wow64,
            "create_time": process_tree.create_time,
            "exit_time": process_tree.exit_time,
            "file_output": process_tree.file_output,
        }

class ProcessHiddenMapperToDict:
    def to_dict(self, process_hidden: ProcessHidden) -> dict:
        return {
            "pid": process_hidden.pid,
            "ppid": process_hidden.ppid,
            "image_file_name": process_hidden.image_file_name,
            "offset": process_hidden.offset,
            "threads": process_hidden.threads,
            "handles": process_hidden.handles,
            "session_id": process_hidden.session_id,
            "wow64": process_hidden.wow64,
            "create_time": process_hidden.create_time,
            "exit_time": process_hidden.exit_time,
            "file_output": process_hidden.file_output,
        }


class ProcessCommandLineMapperToDict:
    def to_dict(self, process_command_line: ProcessCommandLine) -> dict:
        return {
            "pid": process_command_line.pid,
            "process": process_command_line.process,
            "args": process_command_line.args
        }


class ProcessEnvironmentVarsMapperToDict:
    def to_dict(self, process_environment_vars: ProcessEnvironmentVars) -> dict:
        return {
            "pid": process_environment_vars.pid,
            "process": process_environment_vars.process,
            "block": process_environment_vars.block,
            "variable": process_environment_vars.variable,
            "value": process_environment_vars.value
        }