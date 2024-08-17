from blogs.frontend.entities import Trim
import typing as T

if T.TYPE_CHECKING:
    pass

from mock.default.stack.namespace import Module


class Frames(Module):
    class Views:
        class DashboardFrame:
            root = dict(
                __TopBar=dict(
                    create_blog_button="Blogs.Components.CreateBlogButton",
                    account_menu=None,
                )
            )

    class Components:
        class ActionButton:
            trim: Trim

        class DialogButton:
            trim: Trim

        class ToolButton:
            trim: Trim
