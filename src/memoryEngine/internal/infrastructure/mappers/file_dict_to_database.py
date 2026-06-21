from src.memoryEngine.internal.infrastructure.models.file_model import *


class FileScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> FileScanModel:
        return FileScanModel(
            offset = str(raw_data.get("Offset", "")),
            name = str(raw_data.get("Name", ""))
        ).model_dump()


class FileDumpMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> FileDumpModel:
        return FileDumpModel(
            cache=str(raw_data.get("Cache", "")),
            file_object=str(raw_data.get("Fileobject", "")),
            file_name=str(raw_data.get("FileName", "")),
            result=str(raw_data.get("Result", ""))
        ).model_dump()