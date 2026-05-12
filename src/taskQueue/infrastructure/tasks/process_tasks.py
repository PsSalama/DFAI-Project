from src.taskQueue.infrastructure.config.celery_app import celery_app
from src.taskQueue.infrastructure.executors.volatility_executor import run_volatility
import logging


logger = logging.getLogger(__name__)

@celery_app.task(bind=True, name="process_list_task")
def process_list_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise


@celery_app.task(bind=True, name="process_tree_task")
def process_tree_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise


@celery_app.task(bind=True, name="process_hidden_task")
def process_hidden_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise


@celery_app.task(bind=True, name="process_rootkit_task")
def process_rootkit_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise

#######################################################
#######################################################

@celery_app.task(bind=True, name="process_cmdline_task")
def process_cmdline_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise


@celery_app.task(bind=True, name="process_envars_task")
def process_envars_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise


@celery_app.task(bind=True, name="process_thrdscan_task")
def process_thrdscan_task(self, file_path: str, plugin: str):
    logger.info(f"📋 Task {self.request.id}: Processing {plugin} on {file_path}")
    try:
        output_file = f"{plugin.replace('.', '_')}.txt"
        result = run_volatility(file_path, plugin, output_file)

        return {
            "status": "success",
            "task_id": self.request.id,
            "plugin": plugin,
            "file_path": file_path,
            "result": result
        }
    except Exception as e:
        logger.error(f"Task failed: {str(e)}")
        raise