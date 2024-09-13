from projects.models import Project
from dataclassy import dataclass


@dataclass
class DeleteProjectsForm:
    project_ids: list[str]


def delete_projects(form: DeleteProjectsForm):
    projects = Project.objects.filter(id__in=form.project_ids)
    deleted_count, _ = projects.delete()
    return deleted_count
