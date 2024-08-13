from landler.backend.app import *
from landler.frontend.app import *
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_scenario,
    preregister,
    the,
)

from . import factories as F
from sunya.scenarios.store import get_entities


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        e = get_entities()
        preregister("user")

        with add_goal("sign up as a", e.user):
            with the(e.user).visits_the(sign_up_route):
                with the(frontend).calls_the(sign_up_user_api_view).with_the(
                    F.sign_up_request(e)
                ):
                    with the(sign_up_user_api_view).calls_the(
                        create_user_action
                    ).with_the(F.create_user_form(e)):
                        with the(create_user_action).validates_the(e.create_user_form):
                            pass

                        with the(create_user_action).creates_the(e.user):
                            F.user(e)

                    with sign_up_user_api_view_activates_the_user_account(e):
                        e.user.is_active = True

        with add_goal("sign in as a", e.user):
            with the(e.user).visits_the(sign_in_route):
                with the(frontend).calls_the(sign_in_user_api_view).with_the(
                    F.sign_in_request(e)
                ):
                    with the(sign_in_user_api_view).calls_the(sign_in_user_action):
                        user_session.user = e.user
                        e.user.is_authenticated = True

        organization = preregister("organization")
        with add_goal("create an", e.organization, "with admin", user_session.user):
            with the(e.user).visits_the(user_account_route):
                with the(frontend).calls_the(create_organization_api_view).with_the(
                    F.create_organization_request(e)
                ):
                    with the(create_organization_api_view).calls_the(
                        create_organization_action
                    ).with_the(F.create_organization_form(e)):
                        with the(create_organization_action).creates_the(
                            e.organization
                        ):
                            F.organization(e)

                            with the(create_organization_action).calls_the(
                                add_user_to_organization_action
                            ):
                                e.organization.memberships = [F.admin_membership(e)]

        with the_user_switches_to_their_organization_route(user, organization):
            with the(e.user).is_redirected_to(organization_route):
                pass

            with add_goal("set", e.organization, "as the active organization"):
                with the(frontend).calls_the(set_active_organization_api_view).with_the(
                    F.set_active_organization_request(e)
                ):
                    with add_step(
                        "The",
                        set_active_organization_api_view,
                        "updates the",
                        user_session,
                        "to set the active",
                        organization,
                    ):
                        user_session.active_organization = e.organization

    return get_scenario(scenario_name)


def sign_up_user_api_view_activates_the_user_account(e):
    return add_step(
        "The",
        e.user_api_view,
        "activates the account of the",
        e.user,
    )


def the_user_switches_to_their_organization_route(e):
    return add_step(
        "The",
        e.user,
        "uses the",
        organization_picker,
        "to switch to the",
        organization_route,
        "of the",
        e.organization,
    )


def run():
    return start()


if __name__ == "__main__":
    run()
