import landler.backend.namespace as B
import landler.frontend.namespace as F
from sunya import add_goal, add_scenario, get_scenario, register, the, G as g

from sunya.scenarios.store import get_entities


g.sign_up_route = F.Route()
g.sign_in_route = F.Route()
g.user_account_route = F.Route()
g.organization_route = F.Route()


def start():
    scenario_name = "a-user-signs-up-and-creates-an-org"
    with add_scenario(scenario_name):
        e = get_entities()

        with add_goal("sign up as a", e.user):
            with the(e.user).visits_the(g.sign_up_route):
                with the(g.frontend).calls_the(g.sign_up_user_api_view):
                    with the(g.sign_up_user_api_view).calls_the(g.create_user_action):
                        with the(g.create_user_action).creates_the(e.user):
                            user_(e)

                    with the(e.sign_up_user_api_view).activates_the_account_of_the(
                        e.user
                    ):
                        e.user.is_active = True

        with add_goal("sign in as a", e.user):
            with the(e.user).visits_the(g.sign_in_route):
                with the(g.frontend).calls_the(g.sign_in_user_api_view):
                    with the(g.sign_in_user_api_view).calls_the(g.sign_in_user_action):
                        g.user_session.user = e.user
                        e.user.is_authenticated = True

        with add_goal("create an", e.organization, "with admin", g.user_session.user):
            with the(e.user).visits_the(g.user_account_route):
                with the(g.frontend).calls_the(g.create_organization_api_view):
                    with the(g.create_organization_api_view).calls_the(
                        g.create_organization_action
                    ):
                        with the(g.create_organization_action).creates_the(
                            e.organization
                        ):
                            organization_(e)

                        with the(g.create_organization_action).calls_the(
                            g.add_user_to_organization_action
                        ):
                            e.organization.memberships = [admin_membership_(e)]

        with (
            the(e.user)
            .uses_the(g.organization_picker)
            .to_switch_to_the(g.organization_route)
            .of_the(e.organization)
        ):
            with the(e.user).is_redirected_to_the(g.organization_route):
                pass

            with add_goal("set", e.organization, "as the active organization"):
                with the(g.frontend).calls_the(g.set_active_organization_api_view):
                    with (
                        the(g.set_active_organization_api_view)
                        .updates_the(g.user_session)
                        .to_set_the_active(e.organization)
                    ):
                        g.user_session.active_organization = e.organization

    return get_scenario(scenario_name)


def admin_membership_(e):
    return B.Organizations.Models.OrganizationMembership(
        organization=e.organization,
        user=g.user_session.user,
        role=B.Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def organization_(e):
    return register(
        B.Organizations.Models.Organization(name="my-org"),
        e.organization,
    )


def user_(e):
    return register(
        B.Users.Models.User(
            email="my-org-owner@example.com",
            password="my-password",
        ),
        e.user,
    )


def run():
    return start()


if __name__ == "__main__":
    run()
