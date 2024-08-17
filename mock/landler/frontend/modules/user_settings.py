from landler.stack.namespace import Module
from blogs.frontend.entities import Route, Component
from sunya import G as g


class UserSettings(Module):
    class Views:
        class UserSettingsPage(Component):
            root = dict(
                __LeftSideBar=dict(user_settings_side_bar=None),
                __RightCanvas=dict(user_account_canvas=None),
            )

        class UserSettingsNavBar(Component):
            class UserSettingsNavBarItem(Component):
                pass

        class UserProfileView(Component):
            pass

        class UserOrganizationsView(Component):
            pass

    class Routes:
        class UserSettings(Route):
            pass

        class UserProfile(Route):
            pass

        class UserOrganizations(Route):
            pass


g.user_settings = UserSettings.Routes.UserSettings()
g.user_profile = UserSettings.Routes.UserProfile()
g.user_organizations = UserSettings.Routes.UserOrganizations()
g.user_settings_page = UserSettings.Views.UserSettingsPage()
