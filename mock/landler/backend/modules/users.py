from landler.backend.entities import Action, ApiView
from landler.stack.entities import Form, Module
from sunya import actor_to_str, EntityWithId, G as g


class Users(Module):
    class Models:
        class User(EntityWithId):
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

    class ApiViews:
        class SignUpUserApiView(ApiView):
            pass

        class SignInUserApiView(ApiView):
            pass

        class SetActiveOrganizationApiView(ApiView):
            pass

    class DomainEvents:
        class UserCreated:
            user: "Users.Models.User"


g.sign_up_user_api_view = Users.ApiViews.SignUpUserApiView()
g.sign_in_user_api_view = Users.ApiViews.SignInUserApiView()
g.create_user_action = Users.Actions.CreateUser()
g.sign_in_user_action = Users.Actions.SignInUser()
g.set_active_organization_api_view = Users.ApiViews.SetActiveOrganizationApiView()


@actor_to_str.method((Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"
