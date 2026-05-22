from pydantic import BaseModel


class MemoryInfoModel(BaseModel):
    kernel_base: str
    dtb: str
    symbols: str
    is64Bit: str
    isPAE: str
    layer_name: str
    memory_layer: str
    kd_version_block: str
    major_minor: str
    machine_type: str
    ke_number_processors: str
    system_time: str
    nt_system_root: str
    nt_product_type: str
    nt_major_version: str
    nt_minor_version: str
    pe_major_operating_system_version: str
    pe_minor_operating_system_version: str
    pe_machine: str
    pe_time_date_stamp: str