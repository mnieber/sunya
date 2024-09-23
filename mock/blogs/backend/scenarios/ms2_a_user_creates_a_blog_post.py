import blogs.backend.namespace as B
from sunya import (
    G as g,
    add_goal,
    add_scenario,
    run_scenario,
    add_actor,
    get_scenario,
    get_scenario_name,
    the,
    add_role,
)


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start(a_user, a_blog):
    blog_post = add_role("BlogPost")
    blog = add_role("Blog")
    user = add_role("User")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")
        blog.actor = add_actor(a_blog, name="blog")

        with add_goal("create a", blog_post, "in the", blog):
            with the(g.create_blog_post_api_view).calls_the(g.create_blog_post_action):
                blog_post.actor = blog_post_(blog)

    return get_scenario(scenario_name)


def blog_post_(blog):
    return add_actor(
        B.Blogs.Models.BlogPost(
            blog=blog,
            title="My Blog Post",
            content="Hello people",
        ),
        name="blog_post",
    )


def run():
    from . import ms1_a_user_creates_a_blog

    ms1_scenario = run_scenario(ms1_a_user_creates_a_blog)
    a_user = ms1_scenario.get_entity_by_name("user")
    a_blog = ms1_scenario.get_entity_by_name("blog")

    return start(a_user, a_blog)


if __name__ == "__main__":
    run()
