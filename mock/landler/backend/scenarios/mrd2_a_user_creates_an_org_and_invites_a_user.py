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
    organization = add_role("Organization")
    create_org_checklist_item = add_role("CreateOrgChecklistItem")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")
        create_org_checklist_item.actor = B.get_checklist_item("Add your organization")

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
                        B.create_admin_membership(
                            organization.actor,
                            display_name="hello-tim",
                            member_email=f"tim@{organization.actor.name}.com",
                        )
                    ]

            with (
                the(g.create_organization_api_view)
                .calls_the(g.update_checklist_item_action)
                .to_mark_the(create_org_checklist_item)
                .as_completed()
            ):
                with the(g.update_checklist_item_action).updates_the(
                    create_org_checklist_item
                ):
                    create_org_checklist_item.actor.is_completed = True

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
                    g.user_session.active_organization = organization.actor

    return get_scenario(scenario_name)


def organization_():
    return add_actor(
        B.Organizations.Models.Organization(name="my-org"), name="organization"
    )


def run():
    from . import mrd1_a_user_signs_up_and_sees_a_checklist

    mrd1_scenario = run_scenario(mrd1_a_user_signs_up_and_sees_a_checklist)
    a_user = mrd1_scenario.get_entity_by_name("user")

    return start(a_user)


if __name__ == "__main__":
    run()
