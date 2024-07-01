from domain.app import *
from domain.datatypes import *
from sunya import add_step


def the_fe_posts_to_sign_in_a_user(user):
    request = Request(url="/api/session/sign-in/")

    with add_step(
        "The",
        sign_in_page,
        "makes a",
        request,
        "to the",
        sign_in_user_api_view,
    ):
        user_session.user = user
        user.is_authenticated = True

    return user
