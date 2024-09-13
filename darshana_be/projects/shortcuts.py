from projects.models import Project
from rest_framework.exceptions import ValidationError


def get_project_or_400(project_key):
    kwargs = {"pk": project_key}

    project = Project.objects.filter(**kwargs).first()
    if not project:
        raise ValidationError(code="PROJECT_NOT_FOUND")

    return project
