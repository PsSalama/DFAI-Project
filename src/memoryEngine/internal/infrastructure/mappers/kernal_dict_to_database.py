from src.memoryEngine.internal.infrastructure.models.kernal_model import *


class kernalMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> KernalModel:
        return KernalModel(
            index = str(raw_data.get("Index", "")),
            address = str(raw_data.get("Address", "")),
            module = str(raw_data.get("Module", "")),
            symbol = str(raw_data.get("Symbol", "")),
        ).model_dump()
