import typing as T
from .blogs import Blogs

if T.TYPE_CHECKING:
    pass

from blogs.frontend.app import Module, Trim


class Frames(Module):
    class Views:
        class DashboardFrame:
            class __TopBar:
                NewBlogButton: Blogs.Components.NewBlogButton
                AccountMenu: T.Any

    class Components:
        class ActionButton:
            trim: Trim

        class DialogButton:
            trim: Trim

        class ToolButton:
            trim: Trim
