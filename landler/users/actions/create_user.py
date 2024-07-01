from dataclassy import dataclass

from users.models import User


@dataclass
class CreateUserForm:
    email: str


def create_user(create_user_form: CreateUserForm):
    _validate_args(create_user_form)

    user = User(email=create_user_form.email)
    user.save()

    return user


def _validate_args(create_user_form: CreateUserForm):
    if User.objects.filter(email=create_user_form.email).exists():
        raise UserWithEmailAlreadyExistsError()


class UserWithEmailAlreadyExistsError(Exception):
    pass
