from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.app.dto.memory_file_request import MemoryFileRequest
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator
from src.memoryHandling.app.services.process.process_task_service import ProcessTaskService
from src.memoryHandling.injector.injectors import inject_process_task_service

router = APIRouter()

@router.post("/memory_file")
async def memory_file(
    memory_file_request: MemoryFileRequest,
    service: ProcessTaskService = Depends(inject_process_task_service)
):
    validator_result = DumpFileValidator.validate(
        memory_file_request.file_path
    )

    if not validator_result.is_valid:
        raise HTTPException(
            status_code=400,
            detail=validator_result.message
        )

    result = await service.process_tasks(
        memory_file_request.file_path
    )

    return result