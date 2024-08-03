import typing as T

if T.TYPE_CHECKING:
    pass

from blogs.frontend.app import Module, Trim, Route


class Frames(Module):
    class Routes:
        class HomePage(Route):
            pass

    class Views:
        class MainView:
            pass

    class Components:
        class ActionButton:
            trim: Trim

        class DialogButton:
            trim: Trim

        class ToolButton:
            trim: Trim
