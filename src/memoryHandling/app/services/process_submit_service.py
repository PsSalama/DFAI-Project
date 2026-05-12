from src.memoryHandling.app.ports.taskQueue.i_task_producer import IProcessTaskProducer
from src.shared.dto.task_request import TaskRequest


class ProcessService:
    def __init__(self, producer: IProcessTaskProducer):
        self.producer = producer


    async def process_tasks(self, file_path: str) -> dict:
        await self.process_list_task(file_path)
        await self.process_tree_task(file_path)
        await self.process_hidden_task(file_path)
        await self.process_rootkit_task(file_path)
        await self.process_cmdline_task(file_path)
        await self.process_envars_task(file_path)
        await self.process_thrdscan_task(file_path)
        return {
            "request_status": "success"
        }


    async def process_list_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_list_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.pslist"
            }
        )
        return await self.producer.process_list_task(new_task)


    async def process_tree_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_tree_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.pstree"
            }
        )
        return await self.producer.process_tree_task(new_task)


    async def process_hidden_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_hidden_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.psscan"
            }
        )
        return await self.producer.process_hidden_task(new_task)


    async def process_rootkit_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_rootkit_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.psxview"
            }
        )
        return await self.producer.process_rootkit_task(new_task)


############################################################################################
################################# Below is Testing #########################################

    async def process_cmdline_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_cmdline_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.cmdline"
            }
        )
        return await self.producer.process_rootkit_task(new_task)


    async def process_envars_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_envars_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.envars"
            }
        )
        return await self.producer.process_rootkit_task(new_task)


    async def process_thrdscan_task(self, file_path: str) -> dict:
        new_task = TaskRequest(
            task_name = "process_thrdscan_task",
            payload={
                "file_path": file_path,
                "plugin": "windows.thrdscan"
            }
        )
        return await self.producer.process_rootkit_task(new_task)