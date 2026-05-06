from src.memoryHandling.app.services.process.process_list_service import ProcessListService
from src.memoryHandling.app.dtos.memory_file_dto import *
from src.memoryHandling.injector.process_dependencies import get_process_service
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/memory_file")
def memory_file(file_path: MemoryFilePath, process_list_service: ProcessListService = Depends(get_process_service)):
    process_list_service.process_handling(file_path.file_path)
