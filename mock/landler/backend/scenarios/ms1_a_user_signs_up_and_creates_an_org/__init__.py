from landler.backend.app import *
from landler.frontend.app import *
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    register,
    preregister,
    the,
)

from sunya.scenarios.store import get_entities


sign_up_route = Route()
sign_in_route = Route()
user_account_route = Route()
organization_route = Route()


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        e = get_entities()
        preregister("user")

        with add_goal("sign up as a", e.user):
            with the(e.user).visits_the(sign_up_route):
                with the(frontend).calls_the(sign_up_user_api_view):
                    with the(sign_up_user_api_view).calls_the(create_user_action):
                        with the(create_user_action).creates_the(e.user):
                            user_(e)

                    with the(e.user_api_view).activates_the_account_of_the(e.user):
                        e.user.is_active = True

        with add_goal("sign in as a", e.user):
            with the(e.user).visits_the(sign_in_route):
                with the(frontend).calls_the(sign_in_user_api_view):
                    with the(sign_in_user_api_view).calls_the(sign_in_user_action):
                        user_session.user = e.user
                        e.user.is_authenticated = True

        organization = preregister("organization")
        with add_goal("create an", e.organization, "with admin", user_session.user):
            with the(e.user).visits_the(user_account_route):
                with the(frontend).calls_the(create_organization_api_view):
                    with the(create_organization_api_view).calls_the(
                        create_organization_action
                    ):
                        with the(create_organization_action).creates_the(
                            e.organization
                        ):
                            organization_(e)

                            with the(create_organization_action).calls_the(
                                add_user_to_organization_action
                            ):
                                e.organization.memberships = [admin_membership_(e)]

        with (
            the(e.user)
            .uses_the(organization_picker)
            .to_switch_to_the(organization_route)
            .of_the(e.organization)
        ):
            with the(e.user).is_redirected_to_the(organization_route):
                pass

            with add_goal("set", e.organization, "as the active organization"):
                with the(frontend).calls_the(set_active_organization_api_view):
                    with (
                        the(set_active_organization_api_view)
                        .updates_the(user_session)
                        .to_set_the_active(organization)
                    ):
                        user_session.active_organization = e.organization

    return get_scenario(scenario_name)


def admin_membership_(e):
    return Organizations.Models.OrganizationMembership(
        organization=e.organization,
        user=user_session.user,
        role=Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def organization_(e):
    return register(
        Organizations.Models.Organization(name="my-org"),
        e.organization,
    )


def user_(e):
    return register(
        Users.Models.User(
            email="my-org-owner@example.com",
            password="my-password",
        ),
        e.user,
    )


def run():
    return start()


if __name__ == "__main__":
    run()
