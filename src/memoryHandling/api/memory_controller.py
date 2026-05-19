from fastapi import APIRouter, Depends, HTTPException

from src.memoryHandling.app.services.main_service import MainService
from src.memoryHandling.app.dto.memory_file_request import MemoryFileRequest
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator
from src.memoryHandling.injector.injectors import (
    inject_process_task_service,
    inject_registry_task_service,
    inject_dll_task_service,
    inject_activity_task_service,
    inject_privilege_task_service
)


router = APIRouter()

def inject_main_service(
    process_service = Depends(inject_process_task_service),
    registry_service = Depends(inject_registry_task_service),
    dll_service = Depends(inject_dll_task_service),
    activity_service = Depends(inject_activity_task_service),
    privilege_service = Depends(inject_privilege_task_service)
):
    return MainService(process_service, registry_service, dll_service, activity_service, privilege_service)



@router.post("/memory_file")
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