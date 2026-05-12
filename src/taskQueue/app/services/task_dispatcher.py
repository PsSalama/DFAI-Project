from src.taskQueue.app.ports.i_task_queue import (ITaskQueue)
from src.taskQueue.app.dto.task_request import (TaskRequest)


class TaskDispatcher:
    def __init__(self, task_queue: ITaskQueue):
        self.task_queue = task_queue

    async def dispatch(self, task: TaskRequest):
        return await self.task_queue.submit_task(task)