from src.memoryEngine.internal.infrastructure.models.handle_model import *


class HandleMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> HandleModel:
        return HandleModel(
            pid = str(raw_data.get("PID", "")),
            process = str(raw_data.get("Process", "")),
            offset = str(raw_data.get("Offset", "")),
            handle_value = str(raw_data.get("HandleValue", "")),
            type = str(raw_data.get("Type", "")),
            granted_access = str(raw_data.get("GrantedAccess", "")),
            name = str(raw_data.get("Name", ""))
        ).model_dump()