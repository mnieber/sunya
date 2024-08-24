from default.frontend.namespace import Component
from sunya import actor_to_str
from sunya.utils import type_name_to_kebab
import typing as T

if T.TYPE_CHECKING:
    pass

from default.stack.namespace import Module


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
        class ActionButton(Component):
            props = dict(trim="")

        class DialogButton(Component):
            props = dict(trim="")

        class ToolButton(Component):
            props = dict(trim="")


@actor_to_str.method((Frames.Components.ActionButton,))
def action_button_to_str(action_button):
    return f"{type_name_to_kebab(action_button)}:action_button"


@actor_to_str.method((Frames.Components.DialogButton,))
def dialog_button_to_str(dialog_button):
    return f"{type_name_to_kebab(dialog_button)}:dialog_button"


@actor_to_str.method((Frames.Components.ToolButton,))
def tool_button_to_str(tool_button):
    return f"{type_name_to_kebab(tool_button)}:tool_button"
