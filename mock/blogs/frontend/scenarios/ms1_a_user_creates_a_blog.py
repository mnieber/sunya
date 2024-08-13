from blogs.frontend.app import *
from sunya import add_goal, add_scenario, get_scenario, preregister, register, the
from sunya.scenarios.store import get_entities


def start(user):
    scenario_name = "ms1-a-user-creates-a-blog"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        preregister("blog")
        with add_goal("create a", e.blog, "for the", e.user):
            with the(user).visits_the(blogs_route):
                pass

            with the(user).submits_a_form():
                _create_the_create_blog_form()

                with the(frontend).calls_the(create_blog_mutation).with_the(
                    e.create_blog_form
                ):
                    _create_blog(e)

    return get_scenario(scenario_name)


def _create_the_create_blog_form():
    register(Form(name="CreateBlogForm"), name="create_blog_form")


def _create_blog(e):
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
