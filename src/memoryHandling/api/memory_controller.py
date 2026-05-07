from src.memoryHandling.app.services.main_service import MainService
from src.memoryHandling.app.dtos.memory_file_dto import *
from src.memoryHandling.injector.process_dependencies import get_main_service
from fastapi import APIRouter, Depends, HTTPException
from src.memoryHandling.app.validators.dump_file_validator import DumpFileValidator

router = APIRouter()

@router.post("/memory_file")
async def memory_file(
        memory_file_dto: MemoryFileDto,
        main_service: MainService = Depends(get_main_service)
):
    validator_result = DumpFileValidator.validate(memory_file_dto.file_path)
    if not validator_result.is_valid:
        raise HTTPException(
            status_code=400,
            detail=validator_result.message
        )
    return await main_service.main(
        memory_file_dto.project_id,
        memory_file_dto.source_type,
        memory_file_dto.file_path
    )