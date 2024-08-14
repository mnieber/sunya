from blogs.backend.modules import Blogs, Users

from sunya import (
    G as g,
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    register,
    the,
)


def start(user, blog):
    scenario_name = "a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")
        register(blog, name="blog")

        with the(e.user).visits_the(g.blogs_route):
            pass

        with add_goal("create a", e.blog_post, "in the", e.blog):
            with the(e.user).submits_a_form():
                with the(g.frontend).calls_the(g.create_blog_post_api_view):
                    with the(g.create_blog_post_api_view).calls_the(
                        g.create_blog_post_action
                    ):
                        blog_post_(blog, e)

    return get_scenario(scenario_name)


def blog_post_(blog, e):
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
