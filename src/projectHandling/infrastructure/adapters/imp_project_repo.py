from config.database import Database
from src.projectHandling.app.ports.i_project_repo import IProjectRepo
from src.projectHandling.infrastructure.mappers.project_mapper import ProjectMapper


class ImpProjectRepo(IProjectRepo):
    def create_new_project(self, project_info: dict) -> dict:
        project_model = ProjectMapper.dict_to_model(project_info)
        project_document = ProjectMapper.model_to_document(project_model)
        Database.db["projects"].insert_one(project_document)
        return {
            "message": "Project created successfully",
            "project_info": project_document,
        }


    def get_project_by_id(self, project_id: str) -> dict:
        exist_project = Database.db["projects"].find_one({"_id": project_id})
        return exist_project


    def get_all_projects(self) -> list[dict]:
        all_projects = Database.db["projects"].find()
        return list(all_projects)