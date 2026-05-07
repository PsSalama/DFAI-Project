from src.memoryHandling.app.services.process.process_list_service import ProcessListService
from src.memoryHandling.app.dtos.memory_file_dto import *
from src.memoryHandling.injector.process_dependencies import get_process_service
from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator

router = APIRouter()

@router.post("/memory_file")
def memory_file(file_path: MemoryFilePath, process_list_service: ProcessListService = Depends(get_process_service)):
    validator_result = DumpFileValidator.validate(file_path.file_path)
    if not validator_result.is_valid:
        raise HTTPException(
            status_code=400,
            detail=validator_result.message
        )
    return process_list_service.process_handling(file_path.file_path)