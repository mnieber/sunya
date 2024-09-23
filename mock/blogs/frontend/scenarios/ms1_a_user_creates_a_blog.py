import blogs.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    get_scenario_name,
    add_actor,
    the,
    G as g,
    add_role,
)


scenario_name = f"frontend/{get_scenario_name(__file__)}"


def start(a_user):
    blog = add_role("Blog")
    user = add_role("User")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")

        with add_goal("create a", blog, "for the", user):
            with the(user).visits_the(g.blogs_route):
                pass

            with the(user).sees_the(g.blog_list_view):
                pass

            with the(user).presses_the(g.create_blog_button):
                pass

            with the(user).submits_the(g.blog_form_view):
                with the(g.frontend).calls_the(g.create_blog_mutation):
                    blog.actor = blog_()

    return get_scenario(scenario_name)


def blog_():
    return add_actor(
        F.Blogs.Types.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        name="blog",
    )


def run():
    user = F.Users.Types.User(email="alice@example.com")

    return start(user)


if __name__ == "__main__":
    run()
