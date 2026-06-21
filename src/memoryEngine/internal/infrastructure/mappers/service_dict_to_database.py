from src.memoryEngine.internal.infrastructure.models.service_model import *


class ServiceScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> ServiceModel:
        return ServiceModel(
            offset = str(raw_data.get("Offset", "")),
            order = str(raw_data.get("Order", "")),
            pid = str(raw_data.get("PID", "")),
            start = str(raw_data.get("Start", "")),
            state = str(raw_data.get("State", "")),
            type = str(raw_data.get("Type", "")),
            name = str(raw_data.get("Name", "")),
            display = str(raw_data.get("Display", "")),
            binary = str(raw_data.get("Binary", "")),
            binary_registry = raw_data.get("Binary (Registry)", ""),
            dll = str(raw_data.get("Dll", ""))
        ).model_dump()