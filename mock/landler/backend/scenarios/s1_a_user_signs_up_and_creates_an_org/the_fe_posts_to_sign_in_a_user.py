from landler.backend.app import *
from landler.frontend.app import *
from sunya import add_step


def the_fe_posts_to_sign_in_a_user(user):
    request = Request(endpoint="sign-in")

    with add_step(
        "The",
        sign_in_route,
        "makes a",
        request,
        "to the",
        sign_in_user_api_view,
        "to sign in the",
        user,
    ):
        with add_step(
            "The",
            sign_in_user_api_view,
            "calls the",
            sign_in_user_action,
            "to sign in the",
            user,
        ):
            user_session.user = user
            user.is_authenticated = True

    return user
