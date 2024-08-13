from blogs.backend.app import *

from blogs.frontend.modules import blogs_route
from sunya import (
    the,
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    preregister,
    register,
)


def start(user):
    scenario_name = "a-user-creates-a-blog"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        preregister("blog")
        with add_goal("create a", e.blog, "for the", e.user):
            with the(e.user).visits_the(blogs_route):
                pass

            with the(e.user).submits_a_form():
                _create_request()

                with the(frontend).calls_the(create_blog_api_view).with_the(e.request):
                    create_the_create_blog_form(e.request)

                    with the(create_blog_api_view).calls_the(
                        create_blog_action
                    ).with_the(e.create_blog_form):
                        with the(create_blog_action).creates_the(e.blog):
                            _create_blog(e)

    return get_scenario(scenario_name)


def _create_blog(e):
    register(
        Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        e.blog,
    )


def _create_request():
    register(Request(endpoint="create-blog"), name="request")


def create_the_create_blog_form(request):
    register(Form(name="CreateBlogForm", data=request.data), name="create_blog_form")


def run():
    user = Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    return start(user)


if __name__ == "__main__":
    run()
