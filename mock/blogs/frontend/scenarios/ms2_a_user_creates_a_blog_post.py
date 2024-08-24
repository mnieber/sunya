import blogs.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    register,
    the,
    G as g,
    get_entities,
)


def start(user, blog):
    scenario_name = "ms2-a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")
        register(blog, name="blog")

        with add_goal("create a", e.blog_post, "in the", e.blog):
            with the(e.user).visits_the(g.blogs_route):
                pass

            with the(e.user).clicks_on_a(e.blog).to_visit_the(g.blog_route):
                pass

            with the(e.user).presses_the(g.create_blog_post_button):
                pass

            with the(e.user).submits_a_form():
                with the(g.frontend).calls_the(g.create_blog_post_mutation):
                    blog_post_(e)

        with add_goal("edit a", e.blog_post, "in the", e.blog):
            with the(e.user).selects_the(e.blog_post).they_want_to_edit():
                pass

            with the(e.user).presses_the(g.edit_blog_post_button):
                pass

            with the(e.user).submits_a_form():
                with the(g.frontend).calls_the(g.update_blog_post_mutation):
                    e.blog_post.content = "Hello, World!"

        with add_goal("delete a", e.blog_post, "in the", e.blog):
            with the(e.user).selects_the(e.blog_post).they_want_to_delete():
                pass

            with the(e.user).presses_the(g.delete_blog_posts_button):
                pass

    return get_scenario(scenario_name)


def blog_post_(e):
    return register(
        F.Blogs.Types.BlogPost(
            title="My First Blog Post",
            content="Hello",
            blog=e.blog,
            level=F.Blogs.Enums.BlogPostLevel.medium,
        ),
        e.blog_post,
    )


def run():
    from .ms1_a_user_creates_a_blog import run as run_ms1

    ms1_scenario = run_ms1()
    user = ms1_scenario.get_entity_by_name("user")
    blog = ms1_scenario.get_entity_by_name("blog")

    return start(user, blog)


if __name__ == "__main__":
    run()
