from  src.memoryHandling.app.ports.process.i_task_producer import IProcessTaskProducer
from src.shared.dto.task_request import TaskRequest


class MainProcessService:
    def __init__(self, producer: IProcessTaskProducer):
        self.producer = producer


    def main_process_service(self, file_path: str):
        new_task = TaskRequest(
            task_name="process_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.pslist"
            }
        )
        self.producer.process_list_task(new_task)