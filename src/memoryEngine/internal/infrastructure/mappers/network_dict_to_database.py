from src.memoryEngine.internal.infrastructure.models.network_model import *


class NetworkScanMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> NetworkScanModel:
        return NetworkScanModel(
            offset = str(raw_data.get("Offset", "")),
            proto = str(raw_data.get("Proto", "")),
            local_addr = str(raw_data.get("LocalAddr", "")),
            local_port = str(raw_data.get("LocalPort", "")),
            foreign_addr = str(raw_data.get("ForeignAddr", "")),
            foreign_port = str(raw_data.get("ForeignPort", "")),
            state = str(raw_data.get("State", "")),
            pid = str(raw_data.get("PID", "")),
            owner = str(raw_data.get("Owner", "")),
            created = str(raw_data.get("Created", ""))
        ).model_dump()


class NetworkStatMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> NetworkStatModel:
        return NetworkStatModel(
            offset=str(raw_data.get("Offset", "")),
            proto=str(raw_data.get("Proto", "")),
            local_addr=str(raw_data.get("LocalAddr", "")),
            local_port=str(raw_data.get("LocalPort", "")),
            foreign_addr=str(raw_data.get("ForeignAddr", "")),
            foreign_port=str(raw_data.get("ForeignPort", "")),
            state=str(raw_data.get("State", "")),
            pid=str(raw_data.get("PID", "")),
            owner=str(raw_data.get("Owner", "")),
            created=str(raw_data.get("Created", ""))
        ).model_dump()