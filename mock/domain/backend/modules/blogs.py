import typing as T

if T.TYPE_CHECKING:
    pass

from domain.datatypes import Action, ApiView, Enum, Form, Module
from sunya import Entity, actor_to_str, get_actor_key


class Blogs(Module):
    class Models:
        class Blog(Entity):
            name: str
            description: T.Optional[str]

        class BlogPost(Entity):
            blog: "Blogs.Models.Blog"
            title: str
            content: T.Optional[str]

    class Actions:
        class CreateBlog(Action):
            class Args:
                create_blog_form: Form

        class CreateBlogPlot(Action):
            class Args:
                create_blog_post_form: Form
                blog: "Blogs.Models.Blog"

    class Api:
        class CreateBlog(ApiView):
            pass

        class CreateBlogPost(ApiView):
            pass

    class Enums:
        class BlogAudiences(Enum):
            EXPERT = "expert"
            NOVICE = "novice"
            ANY = "any"

    class DomainEvents:
        class BlogCreated:
            pass

        class BlogPostCreated:
            pass


create_blog_action = Blogs.Actions.CreateBlog()
create_blog_post_action = Blogs.Actions.CreateBlog()
create_blog_api_view = Blogs.Api.CreateBlog()
create_blog_post_api_view = Blogs.Api.CreateBlog()


@actor_to_str.method((Blogs.Models.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((Blogs.Models.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.name}+:blog"


@get_actor_key.method((Blogs.Models.Blog,))
def get_blog_key(blog):
    return blog.name


@get_actor_key.method((Blogs.Models.BlogPost,))
def get_blog_post_key(blog_post):
    return blog_post.title
