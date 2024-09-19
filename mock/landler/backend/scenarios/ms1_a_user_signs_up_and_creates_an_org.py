import landler.backend.namespace as B
import landler.frontend.namespace as F  # noqa
from default.frontend.namespace import Route

from sunya import (
    add_goal,
    add_scenario,
    add_role,
    add_actor,
    get_scenario,
    the,
    G as g,
)


g.organization_route = Route()


scenario_name = "backend/ms1-a-user-signs-up-and-creates-an-org"


def start():
    user = add_role("User")
    organization = add_role("Organization")

    with add_scenario(scenario_name):
        with add_goal("sign up as a", user):
            with the(g.sign_up_user_api_view).calls_the(g.create_user_action):
                with the(g.create_user_action).creates_the(user):
                    user.actor = user_()

            with the(g.sign_up_user_api_view).activates_the_account_of_the(user):
                g.user.is_active = True

        with add_goal("sign in as a", user):
            with the(g.sign_in_user_api_view).calls_the(g.sign_in_user_action):
                g.user_session.user = g.user
                g.user.is_authenticated = True

        with add_goal("create an", organization, "with admin", g.user_session.user):
            with the(g.create_organization_api_view).calls_the(
                g.create_organization_action
            ):
                with the(g.create_organization_action).creates_the(organization):
                    organization.actor = organization_()

                with the(g.create_organization_action).calls_the(
                    g.add_user_to_organization_action
                ):
                    g.organization.memberships = [create_admin_membership()]

        with (
            the(user)
            .uses_the(g.organization_picker)
            .in_the(g.frontend)
            .to_switch_to_the(g.organization_route)
            .of_the(organization)
        ):
            with the(user).is_redirected_to_the(g.organization_route):
                pass

            with add_goal("set", organization, "as the active organization"):
                with (
                    the(g.set_active_organization_api_view)
                    .updates_the(g.user_session)
                    .to_set_the_active(organization)
                ):
                    g.user_session.active_organization = organization

    return get_scenario(scenario_name)


def create_admin_membership():
    return B.Organizations.Models.OrganizationMembership(
        organization=g.organization,
        user=g.user_session.user,
        role=B.Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def organization_():
    return add_actor(
        B.Organizations.Models.Organization(name="my-org"), name="organization"
    )


def user_():
    return add_actor(
        B.Users.Models.User(
            email="my-org-owner@example.com",
            password="my-password",
        ),
        name="user",
    )


def run():
    return start()


if __name__ == "__main__":
    run()
