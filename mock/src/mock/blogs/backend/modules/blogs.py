from mock.django_app.namespace import DjangoModule, Action, ApiView, Rule
from mock.python_app.namespace import Form
import typing as T

from sunya import RelatedSet, Entity, FK


class Blogs(DjangoModule):
    class Models:
        class Blog(Entity):
            name: str
            description: T.Optional[str]
            audience: str = "Audiences: expert | novice | any"
            blog_posts: RelatedSet["Blogs.Models.BlogPost"] = []

        class BlogPost(Entity):
            title: str
            content: T.Optional[str]
            blog: FK["Blogs.Models.Blog"]

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

        class UpdateBlogPost(Action):
            class Args:
                update_blog_post_form: Form
                blog_post: "Blogs.Models.BlogPost"

        class DeleteBlogPosts(Action):
            class Args:
                delete_blog_posts_form: Form
                blog_posts: T.List["Blogs.Models.BlogPost"]

    class Rules:
        class HasForbiddenWords(Rule):
            class Args:
                text: str

    class Api:
        class CreateBlogApiView(ApiView):
            pass

        class CreateBlogPostApiView(ApiView):
            pass

        class UpdateBlogApiView(ApiView):
            pass

        class UpdateBlogPostApiView(ApiView):
            pass

        class DeleteBlogPostsApiView(ApiView):
            pass

    class DomainEvents:
        class BlogCreated:
            pass

        class BlogPostCreated:
            pass
