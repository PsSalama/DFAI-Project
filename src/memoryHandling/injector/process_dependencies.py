from fastapi import Depends
# PORTS
from src.memoryHandling.app.ports.database.i_process_repo import IProcessRepo
from src.memoryHandling.app.ports.volatility.i_process_vol import IProcessVol
# ADAPTERS
from src.memoryHandling.infrastructure.adapters.volatility.imp_process_vol import ImpProcesses
from src.memoryHandling.infrastructure.adapters.repositories.imp_process_repo import ImpProcessRepo
# SERVICES
from src.memoryHandling.app.services.main_service import MainService
from src.memoryHandling.app.services.process.process_main_service import ProcessMainService
from src.memoryHandling.app.services.process.process_list_service import ProcessListService
from src.memoryHandling.app.services.process.process_tree_service import ProcessTreeService
from src.memoryHandling.app.services.process.process_hidden_service import ProcessHiddenService
from src.memoryHandling.app.services.process.process_command_line_service import ProcessCommandLineService
from src.memoryHandling.app.services.process.process_environment_vars_service import ProcessEnvironmentVarsService


# =========================
# Infrastructure Adapters
# =========================

def inject_process_vol() -> IProcessVol:
    return ImpProcesses()


def inject_process_repo() -> IProcessRepo:
    return ImpProcessRepo()

# =========================
# Feature Services
# =========================

def get_process_list_service(
    processes: IProcessVol = Depends(inject_process_vol),
    repo: IProcessRepo = Depends(inject_process_repo)
) -> ProcessListService:

    return ProcessListService(
        processes,
        repo
    )


def get_process_tree_service(
    processes: IProcessVol = Depends(inject_process_vol),
    repo: IProcessRepo = Depends(inject_process_repo)
) -> ProcessTreeService:

    return ProcessTreeService(
        processes,
        repo
    )


def get_process_hidden_service(
    processes: IProcessVol = Depends(inject_process_vol),
    repo: IProcessRepo = Depends(inject_process_repo)
) -> ProcessHiddenService:

    return ProcessHiddenService(
        processes,
        repo
    )


def get_process_command_line_service(
    processes: IProcessVol = Depends(inject_process_vol),
    repo: IProcessRepo = Depends(inject_process_repo)
) -> ProcessCommandLineService:

    return ProcessCommandLineService(
        processes,
        repo
    )


def get_process_environment_vars_service(
    processes: IProcessVol = Depends(inject_process_vol),
    repo: IProcessRepo = Depends(inject_process_repo)
) -> ProcessEnvironmentVarsService:

    return ProcessEnvironmentVarsService(
        processes,
        repo
    )

# =========================
# Main Orchestration Service
# =========================

def get_process_main_service(
    process_list_service: ProcessListService = Depends(get_process_list_service),
    process_tree_service: ProcessTreeService = Depends(get_process_tree_service),
    process_hidden_service: ProcessHiddenService = Depends(get_process_hidden_service),
    process_command_line_service: ProcessCommandLineService = Depends(get_process_command_line_service),
    process_environment_vars_service: ProcessEnvironmentVarsService = Depends(get_process_environment_vars_service)
) -> ProcessMainService:

    return ProcessMainService(
        process_list_service,
        process_tree_service,
        process_hidden_service,
        process_command_line_service,
        process_environment_vars_service
    )


# =========================
# Main Application Service
# =========================

def get_main_service(
    process_main_service: ProcessMainService = Depends(get_process_main_service)
) -> MainService:

    return MainService(process_main_service)