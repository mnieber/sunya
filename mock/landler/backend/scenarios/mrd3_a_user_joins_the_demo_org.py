import landler.backend.namespace as B
import landler.frontend.namespace as F  # noqa

from sunya import (
    add_goal,
    add_scenario,
    run_scenario,
    add_role,
    add_actor,
    get_scenario,
    get_scenario_name,
    the,
    G as g,
)

scenario_name = f"backend/{get_scenario_name(__file__)}"


def start(a_user):
    user = add_role("User")
    demo_organization = add_role("DemoOrganization")
    demo_org_checklist_item = add_role("DemoOrgChecklistItem")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")
        demo_org_checklist_item.actor = B.get_checklist_item("Join the demo org")

        with add_goal("add admin", g.user_session.user, "to the", demo_organization):
            with (
                the(g.add_user_to_demo_organization_api_view)
                .calls_the(g.create_organization_action)
                .to_create_the(demo_organization)
            ):
                demo_organization.actor = demo_organization_()

            with the(g.add_user_to_demo_organization_api_view).calls_the(
                g.add_user_to_organization_action
            ):
                demo_organization.actor.memberships = [
                    B.create_admin_membership(
                        demo_organization.actor,
                        display_name="busy-blue-horse",
                        member_email="busybluehorse@demo-org.com",
                    )
                ]

            with (
                the(g.add_user_to_demo_organization_api_view)
                .calls_the(g.update_checklist_item_action)
                .to_mark_the(demo_org_checklist_item)
                .as_completed()
            ):
                with the(g.update_checklist_item_action).updates_the(
                    demo_org_checklist_item
                ):
                    demo_org_checklist_item.actor.is_completed = True

    return get_scenario(scenario_name)


def demo_organization_():
    demo_org = B.Organizations.Models.Organization(name="demo")
    demo_org.staff_settings = B.Organizations.Models.OrganizationStaffSettings(
        organization=demo_org, is_demo_org=True, is_managed_by_tlg=True
    )
    return add_actor(demo_org, name="demo_organization")


def run():
    from . import mrd2_a_user_creates_an_org_and_invites_a_user

    mrd2_scenario = run_scenario(mrd2_a_user_creates_an_org_and_invites_a_user)
    a_user = mrd2_scenario.get_entity_by_name("user")

    return start(a_user)


if __name__ == "__main__":
    run()
