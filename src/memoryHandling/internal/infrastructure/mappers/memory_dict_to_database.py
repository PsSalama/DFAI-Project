from src.memoryHandling.internal.infrastructure.models.memory_model import *


# class MemoryInfoMapperToDatabaseModel:
#     @staticmethod
#     def dict_to_database(raw_data: dict) -> MemoryInfoModel:
#         return MemoryInfoModel(
#             kernel_base = str(raw_data.get("Kernel Base","")),
#             dtb = str(raw_data.get("DTB","")),
#             symbols = str(raw_data.get("Symbols","")),
#             is64Bit = str(raw_data.get("Is64Bit","")),
#             isPAE = str(raw_data.get("IsPAE","")),
#             layer_name = str(raw_data.get("layer_name","")),
#             memory_layer = str(raw_data.get("memory_layer","")),
#             kd_version_block = str(raw_data.get("KdVersionBlock","")),
#             major_minor = str(raw_data.get("Major/Minor","")),
#             machine_type = str(raw_data.get("MachineType","")),
#             ke_number_processors = str(raw_data.get("KeNumberProcessors","")),
#             system_time = str(raw_data.get("SystemTime","")),
#             nt_system_root = str(raw_data.get("NtSystemRoot","")),
#             nt_product_type = str(raw_data.get("NtProductType","")),
#             nt_major_version = str(raw_data.get("NtMajorVersion","")),
#             nt_minor_version = str(raw_data.get("NtMinorVersion","")),
#             pe_major_operating_system_version = str(raw_data.get("PE MajorOperatingSystemVersion","")),
#             pe_minor_operating_system_version = str(raw_data.get("PE MinorOperatingSystemVersion","")),
#             pe_machine = str(raw_data.get("PE Machine","")),
#             pe_time_date_stamp = str(raw_data.get("PE TimeDateStamp",""))
#         ).model_dump()
class MemoryInfoMapperToDatabaseModel:
    @staticmethod
    def dict_to_database(raw_data: dict) -> dict:
        return MemoryInfoModel(
            kernel_base=str(raw_data.get("Kernel Base", "")).strip(),
            dtb=str(raw_data.get("DTB", "")).strip(),
            symbols=str(raw_data.get("Symbols", "")).strip(),
            is64Bit=str(raw_data.get("Is64Bit", "")).strip(),
            isPAE=str(raw_data.get("IsPAE", "")).strip(),
            layer_name=str(raw_data.get("layer_name", "")).strip(),
            memory_layer=str(raw_data.get("memory_layer", "")).strip(),
            kd_version_block=str(raw_data.get("KdVersionBlock", "")).strip(),
            major_minor=str(raw_data.get("Major/Minor", "")).strip(),
            machine_type=str(raw_data.get("MachineType", "")).strip(),
            ke_number_processors=str(raw_data.get("KeNumberProcessors", "")).strip(),
            system_time=str(raw_data.get("SystemTime", "")).strip(),
            nt_system_root=str(raw_data.get("NtSystemRoot", "")).strip(),
            nt_product_type=str(raw_data.get("NtProductType", "")).strip(),
            nt_major_version=str(raw_data.get("NtMajorVersion", "")).strip(),
            nt_minor_version=str(raw_data.get("NtMinorVersion", "")).strip(),

            # Fixed the spaces after "PE " to match Volatility's terminal printout exactly
            pe_major_operating_system_version=str(raw_data.get("PE MajorOperatingSystemVersion", "")).strip(),
            pe_minor_operating_system_version=str(raw_data.get("PE MinorOperatingSystemVersion", "")).strip(),
            pe_machine=str(raw_data.get("PE Machine", "")).strip(),
            pe_time_date_stamp=str(raw_data.get("PE TimeDateStamp", "")).strip()
        ).model_dump()