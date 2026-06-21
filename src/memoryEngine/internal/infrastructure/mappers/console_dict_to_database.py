from src.memoryEngine.internal.infrastructure.models.console_model import *


class ConsoleMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ConsoleModel:
        return ConsoleModel(
            pid = str(raw_data.get("PID", "")),
            process = str(raw_data.get("Process", "")),
            console_info = str(raw_data.get("ConsoleInfo", "")),
            property = str(raw_data.get("Property", "")),
            address = str(raw_data.get("Address", "")),
            data = str(raw_data.get("Data", ""))
        ).model_dump()


class ConsoleCmdScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ConsoleCmdScanModel:
        return ConsoleCmdScanModel(
            pid=str(raw_data.get("PID", "")),
            process=str(raw_data.get("Process", "")),
            console_info=str(raw_data.get("ConsoleInfo", "")),
            property=str(raw_data.get("Property", "")),
            address=str(raw_data.get("Address", "")),
            data=str(raw_data.get("Data", ""))
        ).model_dump()