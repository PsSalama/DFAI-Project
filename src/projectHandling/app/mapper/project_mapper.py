from src.projectHandling.app.dtos.project_info import CreateProjectInfo

class CreateProjectMapper:
    def from_dto_to_dict(self, project_info: CreateProjectInfo) -> dict:
        return {
            "project_name": project_info.project_name,
            "source_type": project_info.source_type,
        }