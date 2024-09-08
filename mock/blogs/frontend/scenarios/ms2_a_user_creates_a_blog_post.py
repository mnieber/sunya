import blogs.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    add_actor,
    the,
    G as g,
    add_role,
)


def start(user, blog):
    blog_post = add_role("BlogPost")
    blog = add_role("Blog")

    scenario_name = "ms2-a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        add_actor(user, name="user")
        add_actor(blog, name="blog", role="Blog")

        with add_goal("create a", blog_post, "in the", g.blog):
            with the(g.user).visits_the(g.blogs_route):
                pass

            with the(g.user).clicks_on_a(blog).to_visit_the(g.blog_route):
                pass

            with the(g.user).presses_the(g.create_blog_post_button):
                pass

            with the(g.user).submits_the(g.blog_post_form_view):
                with the(g.frontend).calls_the(g.create_blog_post_mutation):
                    blog_post_()

        with add_goal("edit a", blog_post, "in the", blog):
            with the(g.user).selects_the(blog_post).they_want_to_edit():
                pass

            with the(g.user).presses_the(g.edit_blog_post_button):
                pass

            with the(g.user).submits_the(g.blog_post_form_view):
                with the(g.frontend).calls_the(g.update_blog_post_mutation):
                    g.blog_post.content = "Hello, World!"

        with add_goal("delete a", blog_post, "in the", blog):
            with the(g.user).selects_the(blog_post).they_want_to_delete():
                pass

            with the(g.user).presses_the(g.delete_blog_posts_button):
                pass

    return get_scenario(scenario_name)


def blog_post_():
    return add_actor(
        F.Blogs.Types.BlogPost(
            title="My First Blog Post",
            content="Hello",
            blog=g.blog,
            level="novice",
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
