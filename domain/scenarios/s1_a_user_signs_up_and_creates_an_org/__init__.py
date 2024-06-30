from mock.app import *
from mock.datatypes import *
from sunya import add_scenario, add_step, get_scenario, preregister

from .the_create_organization_view_calls_the_create_org_action import (
    the_fe_posts_to_create_an_org,
)
from .the_fe_posts_to_sign_in_a_user import the_fe_posts_to_sign_in_a_user
from .the_fe_posts_to_sign_up_a_user import the_fe_posts_to_sign_up_a_user
from .the_fe_redirects_to_the_organization_page_url import (
    the_fe_redirects_to_the_organization_page_url,
)


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        p_user = preregister("user")
        with the_user_visits_the_sign_up_page(p_user):
            user = the_fe_posts_to_sign_up_a_user(p_user)

        with the_user_visits_the_sign_in_page(user):
            the_fe_posts_to_sign_in_a_user(user)

        p_organization = preregister("organization")
        with the_user_visits_the_user_account_page(user, p_organization):
            organization = the_fe_posts_to_create_an_org(p_organization)

        with the_user_switches_to_their_organization_page(user, organization):
            the_fe_redirects_to_the_organization_page_url(user, organization)

    return get_scenario(scenario_name)


def the_user_visits_the_sign_up_page(p_user):
    return add_step(
        "The",
        p_user,
        "visits the",
        sign_up_page,
        "to create a",
        p_user,
    )


def the_user_visits_the_sign_in_page(user):
    return add_step("The", user, "visits the", sign_in_page)


def the_user_visits_the_user_account_page(user, p_organization):
    return add_step(
        "The",
        user,
        "visits the",
        user_account_page,
        "to create an",
        p_organization,
    )


def the_user_switches_to_their_organization_page(user, organization):
    return add_step(
        "The",
        user,
        "uses the",
        organization_picker,
        "to switch to the",
        organization_page,
        "of the",
        organization,
    )


def run():
    return start()


if __name__ == "__main__":
    run()
