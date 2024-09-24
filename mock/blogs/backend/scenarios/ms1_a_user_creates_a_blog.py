import blogs.backend.namespace as B
import blogs.frontend.namespace as F  # noqa

from sunya import (
    the,
    add_goal,
    add_scenario,
    get_scenario,
    get_scenario_name,
    add_actor,
    add_role,
    G as g,
)

scenario_name = f"backend/{get_scenario_name(__file__)}"


def start(a_user):
    user = add_role("User")
    blog = add_role("Blog")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")

        with add_goal("create a", blog, "for the", user):
            with the(g.create_blog_api_view).calls_the(g.create_blog_action):
                with the(g.create_blog_action).runs_the(g.has_forbidden_words_rule):
                    pass

                with the(g.create_blog_action).creates_the(blog):
                    blog.actor = blog_()

    return get_scenario(scenario_name)


def blog_():
    return add_actor(
        B.Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
            audience="any",
        ),
        name="blog",
    )


def run():
    user = B.Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    return start(user)


if __name__ == "__main__":
    run()
