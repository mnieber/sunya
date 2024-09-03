from default.frontend.namespace import Component, Facet, Mutation, Query, Route
from default.stack.namespace import Module, Form
import typing as T

from sunya import EntityWithId, actor_to_str, G as g
from .frames import Frames


class Blogs(Module):
    class Types:
        class Blog(EntityWithId):
            name: str
            description: T.Optional[str]

        class BlogPost(EntityWithId):
            blog: "Blogs.Types.Blog"
            title: str
            content: T.Optional[str]
            isPublished: bool = False
            level: "Blogs.Enums.BlogPostLevel"
            tags: T.List[str] = []

    class Enums:
        class BlogPostLevel:
            easy = "easy"
            medium = "medium"
            hard = "hard"

    class Mutations:
        class CreateBlog(Mutation):
            class Args:
                createBlogForm: Form

        class CreateBlogPost(Mutation):
            class Args:
                createBlogPostForm: Form
                blog: "Blogs.Types.Blog"

        class UpdateBlogPost(Mutation):
            class Args:
                updateBlogPostForm: Form
                blog: "Blogs.Types.Blog"

        class DeleteBlogPosts(Mutation):
            class Args:
                deleteBlogPostsForm: Form

    class Queries:
        class GetBlogs(Query):
            pass

        class GetBlogTags(Query):
            class Args:
                inputValue: str

        class GetBlogPosts(Query):
            pass

    class States:
        class BlogsState:
            class Containers:
                class BlogsCtr:
                    data: Facet
                    selection: Facet
                    highlight: Facet

        class BlogPostsState:
            class Containers:
                class BlogPostsCtr:
                    data: Facet
                    addition: Facet
                    deletion: Facet
                    edit: Facet
                    highlight: Facet
                    selection: Facet

    class Routes:
        class Blogs(Route):
            pass

        class Blog(Route):
            pass

    class StateProviders:
        class BlogsStateProvider:
            pass

        class BlogPostsStateProvider:
            pass

    class Views:
        class BlogFormView(Component):
            pass

        class BlogPostFormView(Component):
            pass

        class BlogListView(Component):
            pass

        class BlogPostListView(Component):
            pass

        class BlogsPage:
            root = dict(
                __LeftSideBar=dict(blog_list_view=None),
                __RightCanvas=dict(
                    blog_post_list_view=None,
                    blog_post_form_view=None,
                    create_blog_post_button=None,
                    edit_blog_post_button=None,
                    delete_blog_posts_button=None,
                ),
            )

    class Effects:
        class SelectBlogEffect:
            pass

    class Components:
        class CreateBlogButton(Frames.Components.DialogButton):
            pass

        class CreateBlogPostButton(Frames.Components.DialogButton):
            pass

        class EditBlogPostButton(Frames.Components.DialogButton):
            pass

        class DeleteBlogPostsButton(Frames.Components.DialogButton):
            pass


g.blog_list_view = Blogs.Views.BlogListView()
g.blog_form_view = Blogs.Views.BlogFormView()
g.blog_post_form_view = Blogs.Views.BlogPostFormView()
g.blog_route = Blogs.Routes.Blog()
g.blogs_route = Blogs.Routes.Blogs()
g.create_blog_button = Blogs.Components.CreateBlogButton()
g.create_blog_mutation = Blogs.Mutations.CreateBlog()
g.create_blog_post_button = Blogs.Components.CreateBlogPostButton()
g.create_blog_post_mutation = Blogs.Mutations.CreateBlogPost()
g.delete_blog_posts_action = Blogs.Mutations.DeleteBlogPosts()
g.delete_blog_posts_button = Blogs.Components.DeleteBlogPostsButton()
g.edit_blog_post_button = Blogs.Components.EditBlogPostButton()
g.update_blog_post_mutation = Blogs.Mutations.UpdateBlogPost()


@actor_to_str.method((Blogs.Types.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((Blogs.Types.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.title}+:blog"
