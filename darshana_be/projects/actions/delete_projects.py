from projects.models import Project


def delete_projects(project_ids: list[str]):
    projects = Project.objects.filter(id__in=project_ids)
    deleted_count, _ = projects.delete()
    return deleted_count
