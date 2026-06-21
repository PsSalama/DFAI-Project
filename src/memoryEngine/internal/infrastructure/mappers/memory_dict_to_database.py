from src.memoryEngine.internal.infrastructure.models.memory_model import *


class MemoryInfoMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> dict:
        return MemoryInfoModel(
            kernel_base=str(raw_data.get("Kernel Base", "")),
            dtb=str(raw_data.get("DTB", "")),
            symbols=str(raw_data.get("Symbols", "")),
            is64Bit=str(raw_data.get("Is64Bit", "")),
            isPAE=str(raw_data.get("IsPAE", "")),
            layer_name=str(raw_data.get("layer_name", "")),
            memory_layer=str(raw_data.get("memory_layer", "")),
            kd_version_block=str(raw_data.get("KdVersionBlock", "")),
            major_minor=str(raw_data.get("Major/Minor", "")),
            machine_type=str(raw_data.get("MachineType", "")),
            ke_number_processors=str(raw_data.get("KeNumberProcessors", "")),
            system_time=str(raw_data.get("SystemTime", "")),
            nt_system_root=str(raw_data.get("NtSystemRoot", "")),
            nt_product_type=str(raw_data.get("NtProductType", "")),
            nt_major_version=str(raw_data.get("NtMajorVersion", "")),
            nt_minor_version=str(raw_data.get("NtMinorVersion", "")),

            # Fixed the spaces after "PE " to match Volatility's terminal printout exactly
            pe_major_operating_system_version=str(raw_data.get("PE MajorOperatingSystemVersion", "")),
            pe_minor_operating_system_version=str(raw_data.get("PE MinorOperatingSystemVersion", "")),
            pe_machine=str(raw_data.get("PE Machine", "")),
            pe_time_date_stamp=str(raw_data.get("PE TimeDateStamp", ""))
        ).model_dump()