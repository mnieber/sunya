import blogs.backend.namespace as B
import blogs.frontend.namespace as F  # noqa

from sunya import (
    the,
    add_goal,
    add_scenario,
    get_scenario,
    add_actor,
    add_role,
    G as g,
)


def start(user):
    blog = add_role("Blog")

    scenario_name = "a-user-creates-a-blog"
    with add_scenario(scenario_name):
        add_actor(user, name="user")

        with add_goal("create a", blog, "for the", g.user):
            with the(g.user).visits_the(g.blogs_route):
                pass

            with the(g.user).submits_the(g.blog_form_view):
                with the(g.frontend).calls_the(g.create_blog_api_view):
                    with the(g.create_blog_api_view).calls_the(g.create_blog_action):
                        with the(g.create_blog_action).creates_the(blog):
                            blog_()

    return get_scenario(scenario_name)


def blog_():
    return add_actor(
        B.Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        name="blog",
        role="Blog",
    )


def run():
    user = B.Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    return start(user)


if __name__ == "__main__":
    run()
