from blogs.frontend.entities import Trim
import typing as T

if T.TYPE_CHECKING:
    from .blogs import Blogs

from blogs.stack.namespace import Module


class Frames(Module):
    class Views:
        class DashboardFrame:
            class __TopBar:
                NewBlogButton: "Blogs.Components.CreateBlogButton"
                AccountMenu: T.Any

    class Components:
        class ActionButton:
            trim: Trim

        class DialogButton:
            trim: Trim

        class ToolButton:
            trim: Trim
