from landler.stack.entities import Module
from blogs.frontend.entities import Route, Component


class UserSettings(Module):
    class Views:
        class UserSettingsPage(Component):
            class __LeftSideBar:
                UserSettingsSideBar = None

            class __RightCanvas:
                UserAccountCanvas = None

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


user_settings = UserSettings.Routes.UserSettings()
user_profile = UserSettings.Routes.UserProfile()
user_organizations = UserSettings.Routes.UserOrganizations()

user_settings_page = UserSettings.Views.UserSettingsPage()
