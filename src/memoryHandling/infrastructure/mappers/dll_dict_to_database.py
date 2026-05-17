from src.memoryHandling.infrastructure.models.dll_model import *


class DllListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DllListModel:
        return DllListModel(
            pid = str(raw_data.get("PID", "")),
            process_base = str(raw_data.get("Process Base", "")),
            size = str(raw_data.get("Size", "")),
            name = str(raw_data.get("Name", "")),
            path = str(raw_data.get("Path", "")),
            load_count = str(raw_data.get("LoadCount", "")),
            load_time = str(raw_data.get("LoadTime", "")),
            file_output = str(raw_data.get("File output", ""))
        ).model_dump()


class DllLdrmodulesMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DllLdrmodulesModel:
        return DllLdrmodulesModel(
            pid = str(raw_data.get("Pid", "")),
            process_base = str(raw_data.get("Process Base","")),
            in_load = str(raw_data.get("InLoad", "")),
            in_init = str(raw_data.get("InInit", "")),
            in_mem = str(raw_data.get("InMem", "")),
            mapped_path = str(raw_data.get("MappedPath"))

        ).model_dump()


class DllModuleMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DllModuleModel:
        return DllModuleModel(
            offset = str(raw_data.get("Offset", "")),
            base = str(raw_data.get("Base", "")),
            size = str(raw_data.get("Size", "")),
            name = str(raw_data.get("Name", "")),
            path = str(raw_data.get("Path", "")),
            file_output = str(raw_data.get("File output", ""))
        ).model_dump()


class DllModscanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DllModscanModel:
        return DllModscanModel(
            offset=str(raw_data.get("Offset", "")),
            base=str(raw_data.get("Base", "")),
            size=str(raw_data.get("Size", "")),
            name=str(raw_data.get("Name", "")),
            path=str(raw_data.get("Path", "")),
            file_output=str(raw_data.get("File output", ""))

        ).model_dump()