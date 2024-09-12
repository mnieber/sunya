from actors.models import Role
from dataclassy import dataclass


@dataclass
class CreateRoleForm:
    name: str


def create_role(create_role_form: CreateRoleForm):
    _validate_args(create_role_form)

    role = Role(
        name=create_role_form.name,
    )
    role.save()

    return role


def _validate_args(create_role_form: CreateRoleForm):
    if Role.objects.filter(name=create_role_form.name).exists():
        raise RoleWithNameAlreadyExistsError()


class RoleWithNameAlreadyExistsError(Exception):
    pass
