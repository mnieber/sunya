from blogs.backend.app import *

from blogs.frontend.modules import blogs_route
from sunya import (
    add_scenario,
    add_goal,
    preregister,
    register,
    get_entities,
)


def start(user):
    scenario_name = "a-user-creates-a-blog"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, alias="user")

        preregister("blog")
        with add_goal("create a", e.blog, "for the", e.user):
            with e.user.visits(blogs_route):
                pass

            with e.user.submits_a_form():
                _create_request()

                with frontend.calls(create_blog_api_view).wth(e.request):
                    create_the_create_blog_form(e.request)

                    with create_blog_api_view.calls(create_blog_action).wth(
                        e.create_blog_form
                    ):
                        with create_blog_action.creates(e.blog):
                            _create_blog(e)


def _create_blog(e):
    register(
        Blogs.Models.Blog(
            name="My Personal Blog",
            description="Random things that interest me",
        ),
        e.blog,
    )


def _create_request():
    register(Request(endpoint="create-blog"), name="request")


def create_the_create_blog_form(request):
    register(Form(name="CreateBlogForm", data=request.data, name="create_blog_form"))


def run():
    user = Users.Models.User(
        email="alice@example.com",
        password="password",
    )

    return start(user)


if __name__ == "__main__":
    run()
