# Module: user_settings

## UserSettings

```python
class UserSettings(ReactModule):
    class Views:
        class UserSettingsPage(Component):
            root: Any = dict(__LeftSideBar=dict(user_settings_side_bar=None), __RightCanvas=dict(user_account_canvas=None))

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
```

