from src.memoryHandling.app.dto.memory_file_request import MemoryFileRequest
from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator
from services.process.main_process_service import MainProcessService
from src.memoryHandling.injector.injectors import *


router = APIRouter()

@router.post("/memory_filee")
async def memory_file(
        memory_file_request: MemoryFileRequest,
        service: MainProcessService = Depends(inject_main_process_service)
):

    validator_result = DumpFileValidator.validate(memory_file_request.file_path)

    if not validator_result.is_valid:
        raise HTTPException(400, validator_result.message)

    service.main_process_service(memory_file_request.file_path)


