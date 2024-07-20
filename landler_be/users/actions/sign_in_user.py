from dataclassy import dataclass
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


@dataclass
class SignInUserForm:
    email: str
    password: str


def sign_in_user(sign_in_user_form: SignInUserForm):
    serializer = TokenObtainPairSerializer(
        data={"email": sign_in_user_form.email, "password": sign_in_user_form.password}
    )
    serializer.is_valid(raise_exception=True)
    if serializer.user and not serializer.user.is_anonymous:
        return serializer.data
    else:
        raise InvalidCredentialsError()


class InvalidCredentialsError(Exception):
    pass
