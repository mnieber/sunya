from domain.app import *
from domain.datatypes import *
from sunya import add_scenario, add_step, get_scenario, preregister, register


def start(user):
    scenario_name = "a-user-creates-a-blog"
    with add_scenario(scenario_name):
        with the_user_visits_the_create_blog_page(user):
            pass

        p_blog = preregister("blog")
        with the_user_submits_a_form_to_create_a_blog(user, p_blog):
            blog = the_fe_posts_to_create_a_blog(user, p_blog)
            assert blog

    return get_scenario(scenario_name)


def the_user_visits_the_create_blog_page(user, p_blog):
    return add_step(
        "The",
        user,
        "visits the",
        create_blog_page,
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


def the_fe_posts_to_create_a_blog(p_blog):
    with add_step(
        "The",
        frontend,
        "posts to the",
        create_blog_api_view,
        "to create a",
        p_blog,
    ):
        with add_step(
            "The",
            create_blog_api_view,
            "calls the",
            create_blog_action,
            "to create a"
            p_blog,
        ):
            blog = register(
                Blogs.Models.Blog(
                    name="My Personal Blog",
                    description="Random things that interest me",
                ),
                p_blog,
            )

    return blog


def run():
    # TODO: create initial actors
    user = None

    return start(user)


if __name__ == "__main__":
    run()
