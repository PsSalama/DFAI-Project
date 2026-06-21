from src.memoryEngine.internal.infrastructure.models.registry_model import *


class RegistryListMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> RegistryListModel:
        return RegistryListModel(
            file_output=str(raw_data.get("File output", "")),
            file_full_path=str(raw_data.get("FileFullPath", "")),
            offset=str(raw_data.get("Offset", ""))

        ).model_dump()


class RegistryScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> RegistryScanModel:
        return RegistryScanModel(
            offset = str(raw_data.get("Offset", ""))
        ).model_dump()


class RegistryKeyMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> RegistryKeyModel:
        return RegistryKeyModel(
            data = str(raw_data.get("Data", "")),
            hive_offset = str(raw_data.get("Hive Offset", "")),
            key = str(raw_data.get("Key", "")),
            last_write_time = str(raw_data.get("Last Write Time", "")),
            name = str(raw_data.get("Name", "")),
            type = str(raw_data.get("Type", "")),
            volatile = str(raw_data.get("Volatile", ""))
        ).model_dump()


class RegistryCertMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> RegistryCertModel:
        return RegistryCertModel(
            certificate_id = str(raw_data.get("Certificate ID", "")),
            certificate_name = str(raw_data.get("Certificate name", "")),
            certificate_path = str(raw_data.get("Certificate path", "")),
            certificate_section = str(raw_data.get("Certificate section", "")),
        ).model_dump()
