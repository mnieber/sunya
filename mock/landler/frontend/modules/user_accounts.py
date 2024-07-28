from landler.stack.entities import Module
from blogs.frontend.entities import Route, Component


class UserAccounts(Module):
    class Components:
        class UserAccountView(Component):
            pass

    class Routes:
        class SignUpRoute(Route):
            pass

        class SignInRoute(Route):
            pass

        class UserAccountRoute(Route):
            pass


sign_up_route = UserAccounts.Routes.SignUpRoute()
sign_in_route = UserAccounts.Routes.SignInRoute()
user_account_route = UserAccounts.Routes.UserAccountRoute()

user_account_view = UserAccounts.Components.UserAccountView()
