from blogs.backend.app import *
from blogs.frontend.modules import blogs_route

from sunya import add_scenario, add_step, get_scenario, preregister, register


def start(user, blog):
    scenario_name = "a-user-creates-a-blog-post"
    with add_scenario(scenario_name):
        p_blog_post = preregister("blog_post")
        with the_user_visits_the_blogs_route(user):
            pass

        with the_user_submits_a_form_to_create_a_blog_post(user, p_blog_post, blog):
            the_fe_posts_to_create_a_blog_post(blog, p_blog_post)

    return get_scenario(scenario_name)


def the_user_visits_the_blogs_route(user):
    return add_step("The", user, "visits the", blogs_route)


def the_user_submits_a_form_to_create_a_blog_post(user, p_blog_post, blog):
    return add_step(
        "The",
        user,
        "submits a form to create a",
        p_blog_post,
        "in the",
        blog,
    )


def the_fe_posts_to_create_a_blog_post(blog, p_blog_post):
    request = Request(endpoint="create-blog-post")

    with add_step(
        "The",
        frontend,
        "makes a",
        request,
        "to the",
        create_blog_post_api_view,
    ):
        create_blog_post_form = Form(name="CreateBlogPostForm")

        with add_step(
            "The",
            create_blog_post_api_view,
            "calls the",
            create_blog_post_action,
            "with the",
            create_blog_post_form,
            "to create the",
            p_blog_post,
        ):
            blog_post = register(
                Blogs.Models.BlogPost(
                    blog=blog,
                    title="My Blog Post",
                    content="Hello people",
                ),
                p_blog_post,
            )

    return blog_post


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
