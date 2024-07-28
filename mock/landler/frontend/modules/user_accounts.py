from landler.stack.entities import Module
from blogs.frontend.entities import Route

from sunya import Entity, actor_to_str


class UserAccounts(Module):
    class Components:
        class UserAccountView(Entity):
            pass

        class OrganizationPicker(Entity):
            pass


sign_up_route = Route(name="sign-up")
sign_in_route = Route(name="sign-in")
user_account_route = Route(name="user-account")
organization_route = Route(name="organization")

user_account_view = UserAccounts.Components.UserAccountView()
organization_picker = UserAccounts.Components.OrganizationPicker()


@actor_to_str.method((UserAccounts.Components.UserAccountView,))
def plot_to_str(user_accounts_view):
    return f":user-accounts-view"


@actor_to_str.method((UserAccounts.Components.OrganizationPicker,))
def organization_picker_to_str(organization_picker):
    return f":organization-picker"
