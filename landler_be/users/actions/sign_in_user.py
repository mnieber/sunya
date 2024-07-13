from dataclassy import dataclass
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


@dataclass
class SignInUserForm:
    email: str
    password: str


def sign_in_user(sign_in_user_form: SignInUserForm):
    user = authenticate(
        email=sign_in_user_form.email, password=sign_in_user_form.password
    )

    if user is None:
        raise InvalidCredentialsError()

    return user


class InvalidCredentialsError(Exception):
    pass
