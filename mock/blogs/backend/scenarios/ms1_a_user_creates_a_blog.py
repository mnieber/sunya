from blogs.backend.app import *

from blogs.frontend.modules import blogs_route
from sunya import (
    the,
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    register,
)


def start(user):
    scenario_name = "a-user-creates-a-blog"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        with add_goal("create a", e.blog, "for the", e.user):
            with the(e.user).visits_the(blogs_route):
                pass

            with the(e.user).submits_a_form():
                with the(frontend).calls_the(create_blog_api_view):
                    with the(create_blog_api_view).calls_the(create_blog_action):
                        with the(create_blog_action).creates_the(e.blog):
                            blog_(e)

    return get_scenario(scenario_name)


def blog_(e):
    register(
        Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        e.blog,
    )


def run():
    user = Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    return start(user)


if __name__ == "__main__":
    run()
