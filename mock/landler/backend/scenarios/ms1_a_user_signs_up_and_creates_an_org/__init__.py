from landler.backend.app import *
from landler.frontend.app import *
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_scenario,
    preregister,
    register,
    the,
)

from sunya.scenarios.store import get_entities


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        e = get_entities()
        preregister("user")

        with add_goal("sign up as a", e.user):
            with the(e.user).visits_the(sign_up_route):
                _create_sign_up_request()

                with the(frontend).calls_the(sign_up_user_api_view).with_the(
                    e.sign_up_request
                ):
                    _create_the_create_user_form()

                    with the(sign_up_user_api_view).calls_the(
                        create_user_action
                    ).with_the(e.create_user_form):
                        with the(create_user_action).validates(e.create_user_form):
                            pass

                        with the(create_user_action).creates_the(e.user):
                            _create_user(e)

                    with sign_up_user_api_view_activates_the_user_account(e):
                        user.is_active = True

        with add_goal("sign in as a", e.user):
            with the(e.user).visits_the(sign_in_route):
                _create_sign_in_request()

                with the(frontend).calls_the(sign_in_user_api_view).with_the(
                    e.sign_in_request
                ):
                    with the(sign_in_user_api_view).calls_the(sign_in_user_action):
                        user_session.user = e.user
                        e.user.is_authenticated = True

        organization = preregister("organization")
        with add_goal("create an", e.organization, "with admin", user_session.user):
            with the(e.user).visits_the(user_account_route):
                _create_the_create_organization_request()

                with the(frontend).calls_the(create_organization_api_view).with_the(
                    e.create_organization_request
                ):
                    _create_the_create_organization_form()

                    with the(create_organization_api_view).calls_the(
                        create_organization_action
                    ).with_the(e.create_organization_form):
                        with the(create_organization_action).creates_the(
                            e.organization
                        ):
                            _create_organization(e)

                            with the(create_organization_action).calls_the(
                                add_user_to_organization_action
                            ):
                                organization.memberships = [
                                    _create_admin_membership(organization)
                                ]

        with the_user_switches_to_their_organization_route(user, organization):
            with the(e.user).is_redirected_to(organization_route):
                pass

            with add_goal("set", e.organization, "as the active organization"):
                _create_set_active_organization_request()

                with the(frontend).calls_the(set_active_organization_api_view).with_the(
                    set_active_organization_request
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


def _create_set_active_organization_request():
    register(
        Request(endpoint="set-active-organization"),
        name="set_active_organization_request",
    )


def _create_admin_membership(e):
    return Organizations.Models.OrganizationMembership(
        organization=e.organization,
        user=user_session.user,
        role=Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def _create_organization(e):
    register(
        Organizations.Models.Organization(name="my-org"),
        e.organization,
    )


def _create_the_create_organization_form(e):
    register(
        Form(name="CreateOrganizationForm", data=e.request.data),
        name="create_organization_form",
    )


def _create_the_create_organization_request():
    register(
        Request(endpoint="create-organization"), name="create_organization_request"
    )


def api_view_activates_the_user_account(e):
    return add_step(
        "The",
        e.user_api_view,
        "activates the account of the",
        e.user,
    )


def _create_sign_in_request():
    register(Request(endpoint="sign-in"), "sign_in_request")


def _create_sign_up_request():
    register(Request(endpoint="sign-up"), name="sign_up_request")


def _create_the_create_user_form(e):
    register(
        Form(name="CreateUserForm", data=e.request.data),
        name="create_user_form",
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


def _create_user(e):
    register(
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
