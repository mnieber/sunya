import typing as T

from projects.models import Project
from dataclassy import dataclass
from django.contrib.auth import get_user_model

from common.utils.arg_utils import optional_args

User = get_user_model()


@dataclass
class CreateProjectForm:
    name: str
    description: T.Optional[str] = None


def create_project(create_project_form: CreateProjectForm):
    _validate_args(create_project_form)

    project = Project(
        name=create_project_form.name,
        **optional_args(description=create_project_form.description)
    )
    project.save()

    return project


def _validate_args(create_project_form: CreateProjectForm):
    if Project.objects.filter(name=create_project_form.name).exists():
        raise ProjectWithNameAlreadyExistsError()


class ProjectWithNameAlreadyExistsError(Exception):
    pass
