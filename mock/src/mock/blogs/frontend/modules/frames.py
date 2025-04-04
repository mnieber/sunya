from kits.react_app.namespace import Component, ReactModule
import typing as T

if T.TYPE_CHECKING:
    pass


class Frames(ReactModule):
    class Views:
        class DashboardFrame:
            root = dict(
                __TopBar=dict(
                    create_blog_button="Blogs.Components.CreateBlogButton",
                    account_menu=None,
                )
            )

    class Components:
        class ActionButton(Component):
            props = dict(trim="")

        class DialogButton(Component):
            props = dict(trim="")

        class ToolButton(Component):
            props = dict(trim="")
