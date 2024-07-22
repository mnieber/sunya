from blogs.frontend.app import *
from sunya import add_scenario, add_step, get_scenario, preregister, register


def start(user):
    scenario_name = "ms1-a-user-creates-a-blog"
    with add_scenario(scenario_name):
        p_blog = preregister("blog")
        with the_user_visits_the_blogs_route(user, p_blog):
            pass

        with the_user_submits_a_form_to_create_a_blog(user, p_blog):
            blog = the_frontend_calls_create_blog_mutation(p_blog)
            assert blog

    return get_scenario(scenario_name)


def the_user_visits_the_blogs_route(user, p_blog):
    return add_step(
        "The",
        user,
        "visits the",
        blogs_route,
        "to create a",
        p_blog,
    )


def the_user_submits_a_form_to_create_a_blog(user, p_blog):
    return add_step(
        "The",
        user,
        "submits a form to create a",
        p_blog,
    )


def the_frontend_calls_create_blog_mutation(p_blog):
    create_blog_form = Form(name="CreateBlogForm")

    with add_step(
        "The",
        frontend,
        "calls the",
        create_blog_mutation,
        "with the",
        create_blog_form,
        "to create a",
        p_blog,
    ):
        blog = register(
            Blogs.Types.Blog(
                name="My Personal Blog",
                description="Random things that interest me",
            ),
            p_blog,
        )

    return blog


def run():
    user = Users.Types.User(email="alice@example.com")

    return start(user)


if __name__ == "__main__":
    run()
