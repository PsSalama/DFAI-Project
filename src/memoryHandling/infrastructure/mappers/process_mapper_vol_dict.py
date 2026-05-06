
class ProcessListMapperToDict:
    def vol_to_dict(self, raw_data: dict) -> dict:
        return {
            "pid": raw_data.get("PID"),
            "ppid": raw_data.get("PPID"),
            "image_file_name": raw_data.get("ImageFileName"),
            "offset": raw_data.get("Offset(V)"),
            "threads": raw_data.get("Threads"),
            "handles": raw_data.get("Handles"),
            "session_id": raw_data.get("SessionId"),
            "wow64": raw_data.get("Wow64"),
            "create_time": raw_data.get("CreateTime"),
            "exit_time": raw_data.get("ExitTime"),
            "file_output": raw_data.get("File output")
        }

class ProcessTreeMapperToDict:
    def vol_to_dict(self, raw_data: dict) -> dict:
        return {
            "pid": raw_data.get("PID"),
            "ppid": raw_data.get("PPID"),
            "image_file_name": raw_data.get("ImageFileName"),
            "offset": raw_data.get("Offset(V)"),
            "threads": raw_data.get("Threads"),
            "handles": raw_data.get("Handles"),
            "session_id": raw_data.get("SessionId"),
            "wow64": raw_data.get("Wow64"),
            "create_time": raw_data.get("CreateTime"),
            "exit_time": raw_data.get("ExitTime"),
            "file_output": raw_data.get("File output")
        }


class ProcessHiddenMapperToDict:
    def vol_to_dict(self, raw_data: dict) -> dict:
        return {
            "pid": raw_data.get("PID"),
            "ppid": raw_data.get("PPID"),
            "image_file_name": raw_data.get("ImageFileName"),
            "offset": raw_data.get("Offset(V)"),
            "threads": raw_data.get("Threads"),
            "handles": raw_data.get("Handles"),
            "session_id": raw_data.get("SessionId"),
            "wow64": raw_data.get("Wow64"),
            "create_time": raw_data.get("CreateTime"),
            "exit_time": raw_data.get("ExitTime"),
            "file_output": raw_data.get("File output")
        }

class ProcessCommandLineMapperToDict:
    def vol_to_dict(self, raw_data: dict) -> dict:
        return {
            "pid": raw_data.get("PID"),
            "ppid": raw_data.get("PPID"),
            "process": raw_data.get("Process"),
            "args": raw_data.get("Args")
        }



class ProcessEnvironmentVarsMapperToDict:
    def vol_to_dict(self, raw_data: dict) -> dict:
        return {
            "pid": raw_data.get("PID"),
            "process": raw_data.get("Process"),
            "block": raw_data.get("Block"),
            "variable": raw_data.get("Variable"),
            "value": raw_data.get("Value")
        }