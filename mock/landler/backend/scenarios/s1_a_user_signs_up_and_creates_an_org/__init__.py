from landler.backend.app import *
from landler.frontend.app import *
from sunya import add_scenario, add_step, get_scenario, preregister, register

from .the_create_organization_view_calls_the_create_org_action import (
    the_fe_posts_to_create_an_org,
)
from .the_fe_redirects_to_the_organization_route import (
    the_fe_redirects_to_the_organization_route,
)


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        p_user = preregister("user")
        with the_user_visits_the_sign_up_route(p_user):
            user = the_fe_posts_to_sign_up_a_user(p_user)

        with the_user_visits_the_sign_in_route(user):
            the_fe_posts_to_sign_in_a_user(user)

        p_organization = preregister("organization")
        with the_user_visits_the_user_account_route(user, p_organization):
            organization = the_fe_posts_to_create_an_org(p_organization)

        with the_user_switches_to_their_organization_route(user, organization):
            the_fe_redirects_to_the_organization_route(user, organization)

    return get_scenario(scenario_name)


def the_user_visits_the_sign_up_route(p_user):
    return add_step(
        "The",
        p_user,
        "visits the",
        sign_up_route,
        "to create a",
        p_user,
    )


def the_user_visits_the_sign_in_route(user):
    return add_step("The", user, "visits the", sign_in_route)


def the_user_visits_the_user_account_route(user, p_organization):
    return add_step(
        "The",
        user,
        "visits the",
        user_account_route,
        "to create an",
        p_organization,
    )


def the_user_switches_to_their_organization_route(user, organization):
    return add_step(
        "The",
        user,
        "uses the",
        organization_picker,
        "to switch to the",
        organization_route,
        "of the",
        organization,
    )


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


def the_fe_posts_to_sign_up_a_user(p_user):
    request = Request(endpoint="sign-up")

    with add_step(
        "The",
        sign_up_route,
        "makes a",
        request,
        "to the",
        sign_up_user_api_view,
    ):
        create_user_form = Form(name="CreateUserForm", data=request.data)
        with add_step(
            "The",
            sign_up_user_api_view,
            "calls the",
            create_user_action,
            "with the",
            create_user_form,
            "to create a",
            p_user,
        ):
            with add_step(
                "The",
                create_user_action,
                "validates the email and password of the",
                create_user_form,
            ):
                pass

            with add_step("The", create_user_action, "creates the", p_user):
                user = register(
                    Users.Models.User(
                        email="my-org-owner@example.com",
                        password="my-password",
                    ),
                    p_user,
                )

        with add_step(
            "The",
            sign_up_user_api_view,
            "activates the account of the",
            user,
        ):
            user.is_active = True

    return user


def run():
    return start()


if __name__ == "__main__":
    run()
