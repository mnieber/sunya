from uuid import UUID

from mock.datatypes import Action, ApiView, Enum, Form, Module
from sunya import Entity, actor_to_str, get_actor_key


class Users(Module):
    class Models:
        class User(Entity):
            """A Django model that contains a user"""

            id: UUID
            email: str
            password: str
            is_authenticated: bool = False

    class Actions:
        class CreateUser(Action):
            class Args:
                create_user_form: Form

    class ApiViews:
        class SignUpUserApiView(ApiView):
            pass

        class SignInUserApiView(ApiView):
            pass

        class SetActiveOrganizationApiView(ApiView):
            pass

    class Enums:
        class UserRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"

    class DomainEvents:
        class UserCreated:
            user: "Users.Models.User"


sign_up_user_api_view = Users.ApiViews.SignUpUserApiView()
sign_in_user_api_view = Users.ApiViews.SignInUserApiView()
create_user_action = Users.Actions.CreateUser()
set_active_organization_api_view = Users.ApiViews.SetActiveOrganizationApiView()


@actor_to_str.method((Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"


@get_actor_key.method((Users.Models.User,))
def get_user_key(user):
    return user.email
