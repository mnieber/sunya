from blogs.backend.app import *
from blogs.frontend.modules import blogs_route

from sunya import (
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    preregister,
    register,
)


def start(user, blog):
    scenario_name = "a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, alias="user")
        register(blog, alias="blog")

        preregister("blog_post")
        with e.user.visits(blogs_route):
            pass

        with add_goal("create a", e.blog_post, "in the", e.blog):
            with user.submits_a_form():
                register(Request(endpoint="create-blog-post"), name="request")

                with frontend.calls(create_blog_post_api_view).wth(e.request):
                    _create_the_create_blog_post_form()

                    with create_blog_post_api_view.calls(create_blog_post_action).wth(
                        e.create_blog_post_form
                    ):
                        _create_blog_post(blog, e)

    return get_scenario(scenario_name)


def _create_the_create_blog_post_form():
    register(Form(name="CreateBlogPostForm"), name="create_blog_post_form")


def _create_blog_post(blog, e):
    register(
        Blogs.Models.BlogPost(
            blog=blog,
            title="My Blog Post",
            content="Hello people",
        ),
        e.blog_post,
    )


def run():
    user = Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    existing_blog = Blogs.Models.Blog(
        name="My Original Blog",
        description="Original description",
    )

    return start(user, existing_blog)


if __name__ == "__main__":
    run()
