import landler.backend.namespace as B
import landler.frontend.namespace as F  # noqa
from default.frontend.namespace import Route

from sunya import (
    add_goal,
    add_scenario,
    run_scenario,
    add_role,
    add_actor,
    get_scenario,
    the,
    G as g,
)


g.organization_route = Route(name="organization")


scenario_name = "backend/ms1-a-user-signs-up-and-creates-an-org"


def start(a_user):
    user = add_role("User")
    organization = add_role("Organization")
    demo_organization = add_role("DemoOrganization")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")

        with add_goal("add admin", g.user_session.user, "to the", demo_organization):
            with the(g.add_user_to_demo_organization_api_view).calls_the(
                g.create_organization_action
            ).to_create_the(demo_organization):
                demo_organization.actor = demo_organization_()

            with the(g.add_user_to_demo_organization_api_view).calls_the(
                g.add_user_to_organization_action
            ):
                demo_organization.actor.memberships = [
                    create_admin_membership(demo_organization.actor)
                ]

        with add_goal("create an", organization, "with admin", g.user_session.user):
            with the(g.create_organization_api_view).calls_the(
                g.create_organization_action
            ):
                with the(g.create_organization_action).creates_the(organization):
                    organization.actor = organization_()

                with the(g.create_organization_action).calls_the(
                    g.add_user_to_organization_action
                ):
                    g.organization.memberships = [
                        create_admin_membership(organization.actor)
                    ]

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


def demo_organization_():
    return add_actor(
        B.Organizations.Models.Organization(name="demo"), name="demo_organization"
    )


def organization_():
    return add_actor(
        B.Organizations.Models.Organization(name="my-org"), name="organization"
    )


def create_admin_membership(organization):
    return B.Organizations.Models.OrganizationMembership(
        organization=organization,
        user=g.user_session.user,
        role=B.Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def run():
    from . import ms1_a_user_signs_up_and_sees_a_checklist

    ms1_scenario = run_scenario(ms1_a_user_signs_up_and_sees_a_checklist)
    a_user = ms1_scenario.get_entity_by_name("user")

    return start(a_user)


if __name__ == "__main__":
    run()
