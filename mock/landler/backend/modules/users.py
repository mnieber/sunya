from default.backend.namespace import Action, ApiView
from default.stack.namespace import Form, Module
from sunya import actor_to_str, EntityWithId, G as g, any_dict
import typing as T

if T.TYPE_CHECKING:
    from landler.backend.modules.checklists import Checklists


class Users(Module):
    class Models:
        class User(EntityWithId):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False

            # Related names (automatically added based on foreign keys)
            checklist: "Checklists.Models.Checklist" = any_dict()

    class Actions:
        class CreateUser(Action):
            class Args:
                create_user_form: Form

        class SignInUser(Action):
            class Args:
                sign_in_user_form: Form

    class ApiViews:
        class SignUpUserApiView(ApiView):
            pass

        class SignInUserApiView(ApiView):
            pass

    class DomainEvents:
        class UserCreated:
            user: "Users.Models.User"


g.sign_up_user_api_view = Users.ApiViews.SignUpUserApiView()
g.sign_in_user_api_view = Users.ApiViews.SignInUserApiView()
g.create_user_action = Users.Actions.CreateUser()
g.sign_in_user_action = Users.Actions.SignInUser()


@actor_to_str.method((Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"
