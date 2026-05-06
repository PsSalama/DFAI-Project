from fastapi import Depends
from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.infrastructure.adapters.volatility.imp_process_vol import ImpProcesses
from src.memoryHandling.infrastructure.adapters.repositories.imp_process_repo import ImpProcessRepo

from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol
from src.memoryHandling.app.services.process.process_list_service import ProcessListService

def get_process_vol() -> IProcessVol:
    return ImpProcesses()

def get_process_repo() -> IProcessRepo:
    return ImpProcessRepo()

def get_process_service(processes: IProcessVol = Depends(get_process_vol), repo: IProcessRepo = Depends(get_process_repo)) -> ProcessListService:
    return ProcessListService(
        processes,
        repo
    )