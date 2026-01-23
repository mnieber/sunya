import typing as T

from projects.models import Project
from dataclassy import dataclass


@dataclass
class UpdateProjectForm:
    name: str
    description: T.Optional[str] = None


def update_project(update_project_form: UpdateProjectForm, project: Project):
    _validate_args(update_project_form, project)

    project.name = update_project_form.name
    project.description = update_project_form.description

    project.save()

    return project


def _validate_args(update_project_form: UpdateProjectForm, project: Project):
    if (
        Project.objects.filter(name=update_project_form.name)
        .exclude(id=project.id)
        .exists()
    ):
        raise ProjectWithNameAlreadyExistsError()


class ProjectWithNameAlreadyExistsError(Exception):
    pass
