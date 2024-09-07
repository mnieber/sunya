import blogs.backend.namespace as B
from sunya import (
    G as g,
    add_goal,
    add_scenario,
    add_actor,
    get_scenario,
    the,
    add_role,
)


def start(user, blog):
    blog_post = add_role("BlogPost")

    scenario_name = "a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        add_actor(user, name="user")
        add_actor(blog, name="blog")

        with add_goal("create a", blog_post, "in the", g.blog):
            with the(g.create_blog_post_api_view).calls_the(g.create_blog_post_action):
                blog_post_(blog)

    return get_scenario(scenario_name)


def blog_post_(blog):
    return add_actor(
        B.Blogs.Models.BlogPost(
            blog=blog,
            title="My Blog Post",
            content="Hello people",
        ),
        name="blog_post",
        role="BlogPost",
    )


def run():
    from .ms1_a_user_creates_a_blog import run as run_ms1

    ms1_scenario = run_ms1()
    user = ms1_scenario.get_entity_by_name("user")
    blog = ms1_scenario.get_entity_by_name("blog")

    return start(user, blog)


if __name__ == "__main__":
    run()
