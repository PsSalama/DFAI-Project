from src.memoryEngine.internal.app.ports.network.i_network_task_producer import INetworkTaskProducer
from src.memoryEngine.internal.app.dto.task_request import TaskRequest


class NetworkTaskService:
    def __init__(self, producer: INetworkTaskProducer):
        self.producer = producer


    async def all_tasks(self, file_path: str) -> dict:
        await self.network_scan_task(file_path)
        await self.network_stat_task(file_path)
        return {
            "request_status": "success"
        }


    async def network_scan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "network_scan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.netscan"
            }
        )
        return await self.producer.network_scan_task(new_task)


    async def network_stat_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "network_stat_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.netstat"
            }
        )
        return await self.producer.network_stat_task(new_task)

