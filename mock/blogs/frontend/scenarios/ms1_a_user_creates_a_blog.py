from blogs.frontend.app import *
from blogs.frontend.modules import *
from sunya import add_goal, add_scenario, get_scenario, register, the, G as g
from sunya.scenarios.store import get_entities


def start(user):
    scenario_name = "ms1-a-user-creates-a-blog"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        with add_goal("create a", e.blog, "for the", e.user):
            with the(e.user).visits_the(g.blogs_route):
                pass

            with the(e.user).submits_a_form():
                with the(g.frontend).calls_the(g.create_blog_mutation):
                    blog_(e)

    return get_scenario(scenario_name)


def blog_(e):
    register(
        Blogs.Types.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        e.blog,
    )


def run():
    user = Users.Types.User(email="alice@example.com")

    return start(user)


if __name__ == "__main__":
    run()
