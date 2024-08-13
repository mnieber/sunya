from blogs.backend.app import *
from blogs.frontend.modules import blogs_route

from sunya import (
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    preregister,
    register,
    the,
)


def start(user, blog):
    scenario_name = "a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")
        register(blog, name="blog")

        preregister("blog_post")
        with the(e.user).visits_the(blogs_route):
            pass

        with add_goal("create a", e.blog_post, "in the", e.blog):
            with the(e.user).submits_a_form():
                register(Request(endpoint="create-blog-post"), name="request")

                with the(frontend).calls_the(create_blog_post_api_view).with_the(
                    e.request
                ):
                    _create_the_create_blog_post_form()

                    with the(create_blog_post_api_view).calls_the(
                        create_blog_post_action
                    ).with_the(e.create_blog_post_form):
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
