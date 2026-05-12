from src.memoryHandling.app.services.process_submit_service import ProcessService
from src.memoryHandling.app.ports.taskQueue.i_task_status_reader import ITaskStatusReader


class WorkflowService:
    def __init__(self,process_service: ProcessService, status_reader: ITaskStatusReader):
        self.process_service = process_service
        self.status_reader = status_reader


    async def start_memory_analysis(self, file_path: str):
        response = await self.process_service.process_tasks(file_path)
        tasks = response["tasks"]
        return tasks


    async def monitor_tasks(self, tasks: list):
        statuses = []
        for task in tasks:
            status = await self.status_reader.get_task_status(
                task["task_id"]
            )
            statuses.append(status)
        return statuses


    async def wait_until_finished(self, tasks: list):
        while True:
            all_finished = True
            for task in tasks:
                status = await self.status_reader.get_task_status(
                    task["task_id"]
                )
                if not status["is_success"]:
                    all_finished = False
            if all_finished:
                break