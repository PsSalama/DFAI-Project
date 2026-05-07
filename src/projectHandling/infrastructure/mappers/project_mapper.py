from src.projectHandling.infrastructure.models.project_model import ProjectModel

class ProjectMapper:
    @staticmethod
    def model_to_document(project_model: ProjectModel) -> dict:
        return {
            "_id": project_model.project_id,
            "project_name": project_model.project_name,
            "source_type": project_model.source_type,
            "created_at": project_model.created_at,
            "updated_at": project_model.updated_at,
            "collections": project_model.collections,
        }

    @staticmethod
    def dict_to_model(project_document: dict) -> ProjectModel:
        return ProjectModel(
            project_name = project_document['project_name'],
            source_type = project_document['source_type'],
        )