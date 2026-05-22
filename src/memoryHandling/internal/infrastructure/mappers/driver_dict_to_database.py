from src.memoryHandling.internal.infrastructure.models.driver_model import *


class DriverScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DriverModel:
        return DriverModel(
            offset = str(raw_data.get("Offset", "")),
            start = str(raw_data.get("Start", "")),
            size = str(raw_data.get("Size", "")),
            service_key = str(raw_data.get("Service Key", "")),
            driver_name = str(raw_data.get("Driver Name", "")),
            name = str(raw_data.get("Name", ""))
        ).model_dump()


class DriverIrpMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> DriverIrpModel:
        return DriverIrpModel(
            offset = str(raw_data.get("Offset", "")),
            driver_name = str(raw_data.get("Driver Name", "")),
            irp = str(raw_data.get("IRP", "")),
            address = str(raw_data.get("Address", "")),
            module = str(raw_data.get("Module", "")),
            symbol = str(raw_data.get("Symbol", ""))
        ).model_dump()