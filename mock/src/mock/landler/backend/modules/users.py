from kits.django_app.impl.namespace import DjangoModule
from sunya import Entity
import typing as T

if T.TYPE_CHECKING:
    pass


class Users(DjangoModule):
    class Models:
        class User(Entity):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False

    class Forms:
        class CreateUserForm:
            email: str
            password: str
            password_confirmation: str

        class SignInUserForm:
            email: str
            password: str

    class DomainEvents:
        class UserCreated:
            user: "Users.Models.User"
