import typing as T

if T.TYPE_CHECKING:
    pass

from blogs.backend.entities import Action, ApiView
from blogs.stack.entities import Enum, Form, Module
from sunya import EntityWithId, actor_to_str


class Blogs(Module):
    class Models:
        class Blog(EntityWithId):
            name: str
            description: T.Optional[str]

        class BlogPost(EntityWithId):
            blog: "Blogs.Models.Blog"
            title: str
            content: T.Optional[str]

    class Actions:
        class CreateBlog(Action):
            class Args:
                create_blog_form: Form

        class CreateBlogPost(Action):
            class Args:
                create_blog_post_form: Form
                blog: "Blogs.Models.Blog"

        class UpdateBlog(Action):
            class Args:
                update_blog_form: Form
                blog: "Blogs.Models.Blog"

    class ApiViews:
        class CreateBlog(ApiView):
            pass

        class CreateBlogPost(ApiView):
            pass

        class UpdateBlog(ApiView):
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
create_blog_api_view = Blogs.ApiViews.CreateBlog()
create_blog_post_api_view = Blogs.ApiViews.CreateBlog()
update_blog_action = Blogs.Actions.UpdateBlog()
update_blog_api_view = Blogs.ApiViews.UpdateBlog()


@actor_to_str.method((Blogs.Models.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((Blogs.Models.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.title}+:blog-post"
