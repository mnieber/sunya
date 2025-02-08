from mock.django_app.namespace import Action, ApiView, DjangoModule
from mock.python_app.namespace import Form
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

    class Actions:
        class CreateUser(Action):
            class Args:
                create_user_form: Form

        class SignInUser(Action):
            class Args:
                sign_in_user_form: Form

        class ActivateUserAccount(Action):
            class Args:
                user: "Users.Models.User"

    class Api:
        class SignUpUserApiView(ApiView):
            pass

        class SignInUserApiView(ApiView):
            pass

    class DomainEvents:
        class UserCreated:
            user: "Users.Models.User"
