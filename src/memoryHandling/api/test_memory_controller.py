from src.memoryHandling.app.dto.memory_file_request import MemoryFileRequest
from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator
from src.memoryHandling.app.services.process_submit_service import ProcessService
from src.memoryHandling.injector.new_process_injector import inject_process_task_producer
from src.memoryHandling.app.ports.taskQueue.i_task_producer import IProcessTaskProducer


router = APIRouter()

@router.post("/memory_filee")
async def memory_file(
        memory_file_request: MemoryFileRequest,
        producer: IProcessTaskProducer = Depends(inject_process_task_producer)
) -> dict:
    validator_result = DumpFileValidator.validate(memory_file_request.file_path)
    if not validator_result.is_valid:
        raise HTTPException(
            status_code=400,
            detail=validator_result.message
        )
    process_service = ProcessService(producer)
    return await process_service.process_tasks(memory_file_request.file_path)