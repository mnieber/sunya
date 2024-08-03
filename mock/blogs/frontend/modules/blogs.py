import typing as T

if T.TYPE_CHECKING:
    pass

from blogs.frontend.app import Module, Mutation, Facet, Route, Query, Form
from sunya import EntityWithId, actor_to_str
from .frames import Frames


class Blogs(Module):
    class Types:
        class Blog(EntityWithId):
            name: str
            description: T.Optional[str]
            tags: T.List[str]

        class BlogPost(EntityWithId):
            blog: "Blogs.Types.Blog"
            title: str
            content: T.Optional[str]
            isPublished: bool
            level: "Blogs.Enums.BlogPostLevel"
            tags: str[]

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
                    display: Facet
                    dragAndDrop: Facet
                    edit: Facet
                    filtering: Facet
                    highlight: Facet
                    insertion: Facet
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
        class BlogPostFormView:
            pass

        class BlogsPage:
            class __LeftSideBar:
                BlogListView: T.Any

            class __RightCanvas:
                BlogPostListView: T.Any
                BlogPostFormView: T.Any
                CreateBlogPostButton: T.Any
                EditBlogPostButton: T.Any
                DeleteBlogPostsButton: T.Any

    class Effects:
        class SelectBlogEffect:
            pass

    class Components:
        class CreateBlogButton(Frames.Components.DialogButton):
            pass

        class CreateBlogPostButton(Frames.Components.ActionButton):
            pass

        class EditBlogPostButton(Frames.Components.ActionButton):
            pass

        class DeleteBlogPostsButton(Frames.Components.ActionButton):
            pass


create_blog_mutation = Blogs.Mutations.CreateBlog()
create_blog_post_mutation = Blogs.Mutations.CreateBlogPost()
delete_blog_posts_action = Blogs.Mutations.DeleteBlogPosts()
blogs_route = Blogs.Routes.Blogs()


@actor_to_str.method((Blogs.Types.Blog,))
def blog_to_str(blog):
    return f"{blog.name}+:blog"


@actor_to_str.method((Blogs.Types.BlogPost,))
def blog_post_to_str(blog_post):
    return f"{blog_post.title}+:blog"
