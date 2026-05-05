from fastapi import FastAPI
from src.memoryHandling.app.services.process.ProcessList import ProcessListService
from src.memoryHandling.app.ports.volatility.IProcesses import IProcesses

app = FastAPI()

@app.post("/memory_path")
def file_path(memory_dump_file_path:str):
    process_list_service = ProcessListService(IProcesses)
    return new_process_list
