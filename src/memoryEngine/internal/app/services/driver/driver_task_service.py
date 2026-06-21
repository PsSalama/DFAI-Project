from src.memoryEngine.internal.app.ports.driver.i_driver_task_producer import IDriverTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class DriverTaskService:
    def __init__(self, producer: IDriverTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.driver_scan_task(file_path)
        await self.driver_irp_task(file_path)
        return {
            "request_status": "success"
        }


    async def driver_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "driver_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.driverscan"
            }
        )
        return await self.producer.driver_scan_task(new_task)


    async def driver_irp_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "driver_irp_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.driverirp"
            }
        )
        return await self.producer.driver_irp_task(new_task)