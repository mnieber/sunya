from sunya import actor_to_str, type_name_to_kebab

import mock.blogs.frontend.impl.namespace as F


@actor_to_str.method((F.Blogs.Types.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((F.Blogs.Types.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.title}+:blog"


@actor_to_str.method((F.Users.Types.User,))
def user_to_str(user):
    return f"{user.email}+:user"


@actor_to_str.method((F.Frames.Components.ActionButton,))
def action_button_to_str(action_button):
    return f"{type_name_to_kebab(action_button)}:action_button"


@actor_to_str.method((F.Frames.Components.DialogButton,))
def dialog_button_to_str(dialog_button):
    return f"{type_name_to_kebab(dialog_button)}:dialog_button"


@actor_to_str.method((F.Frames.Components.ToolButton,))
def tool_button_to_str(tool_button):
    return f"{type_name_to_kebab(tool_button)}:tool_button"
