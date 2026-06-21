from fastapi import APIRouter, Depends, HTTPException

from src.memoryEngine.internal.app.services.main_service import MainService
from src.memoryEngine.internal.app.dto.memory_file_request import MemoryFileRequest
from src.memoryEngine.internal.app.validators.dump_file_validator import DumpFileValidator
from src.memoryEngine.internal.injector.injectors import (
    inject_process_task_service,
    inject_registry_task_service,
    inject_dll_task_service,
    inject_activity_task_service,
    inject_privilege_task_service,
    inject_file_task_service,
    inject_service_task_service,
    inject_driver_task_service,
    inject_memory_task_service,
    inject_network_task_service,
    inject_console_task_service
)


router = APIRouter()

def inject_main_service(
    process_service = Depends(inject_process_task_service),
    registry_service = Depends(inject_registry_task_service),
    dll_service = Depends(inject_dll_task_service),
    activity_service = Depends(inject_activity_task_service),
    privilege_service = Depends(inject_privilege_task_service),
    file_service = Depends(inject_file_task_service),
    service_service = Depends(inject_service_task_service),
    driver_service = Depends(inject_driver_task_service),
    memory_service = Depends(inject_memory_task_service),
    network_service = Depends(inject_network_task_service),
    console_service = Depends(inject_console_task_service)
):
    return MainService(
        process_service,
        registry_service,
        dll_service,
        activity_service,
        privilege_service,
        file_service,
        service_service,
        driver_service,
        memory_service,
        network_service,
        console_service
    )


@router.post("/memory/path")
async def memory_file(
    memory_file_request: MemoryFileRequest,
    main_service: MainService = Depends(inject_main_service)
):
    validator_result = DumpFileValidator.validate(
        memory_file_request.file_path
    )

    if not validator_result.is_valid:
        raise HTTPException(
            status_code=400,
            detail=validator_result.message
        )

    result = await main_service.main_tasks(
        memory_file_request.file_path
    )
    return result

