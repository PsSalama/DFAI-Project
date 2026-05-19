from src.memoryHandling.infrastructure.models.privilege_model import *


class PrivilegeProcessMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> PrivilegeProcessModel:
        return PrivilegeProcessModel(
            pid=str(raw_data.get("PID", "")),
            process=str(raw_data.get("Process", "")),
            value=str(raw_data.get("Value", "")),
            privilege=str(raw_data.get("Privilege", "")),
            attributes=str(raw_data.get("Attributes", "")),
            description=str(raw_data.get("Description", ""))
        ).model_dump()


class PrivilegeServiceIdMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> PrivilegeServiceIdModel:
        return PrivilegeServiceIdModel(
            sid=str(raw_data.get("SID", "")),
            service=str(raw_data.get("Service", "")),
            pdb_scanning_finished=str(raw_data.get("PDB scanning finished", ""))
        ).model_dump()