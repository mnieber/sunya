from domain.datatypes import Module, Page
from sunya import Entity, actor_to_str


class UserAccounts(Module):
    class Components:
        class UserAccountView(Entity):
            pass

        class OrganizationPicker(Entity):
            pass


sign_up_page = Page(host="http://landler.io", path="/sign-up")
sign_in_page = Page(host="http://landler.io", path="/sign-in")
user_account_page = Page(host="http://landler.io", path="/user-account")
organization_page = Page(host="http://my-org.landler.io", path="/home")

user_account_view = UserAccounts.Components.UserAccountView()
organization_picker = UserAccounts.Components.OrganizationPicker()


@actor_to_str.method((UserAccounts.Components.UserAccountView,))
def plot_to_str(user_accounts_view):
    return f":user-accounts-view"


@actor_to_str.method((UserAccounts.Components.OrganizationPicker,))
def organization_picker_to_str(organization_picker):
    return f":organization-picker"
