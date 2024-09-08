import typing as T

from projects.models import Project
from dataclassy import dataclass

from common.utils.arg_utils import optional_args


@dataclass
class SaveProjectForm:
    name: str
    description: T.Optional[str] = None


def save_project(save_project_form: SaveProjectForm, project: Project):
    _validate_args(save_project_form, project)

    project.name = save_project_form.name
    project.description = save_project_form.description

    project.save()

    return project


def _validate_args(save_project_form: SaveProjectForm, project: Project):
    if Project.objects.filter(name=save_project_form.name).exclude(id=project.id).exists():
        raise ProjectWithNameAlreadyExistsError()


class ProjectWithNameAlreadyExistsError(Exception):
    pass
