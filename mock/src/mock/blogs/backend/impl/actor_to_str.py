from sunya import actor_to_str

import mock.blogs.backend.impl.namespace as B


@actor_to_str.method((B.Blogs.Models.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((B.Blogs.Models.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.title}+:blog-post"


@actor_to_str.method((B.Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"
