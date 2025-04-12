from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
    comment,
    G as g,
    R as r,
    I as i,
)

scenario_name = f"backend/mrd3_a_user_joins_the_demo_org"


def start():
    with add_scenario(scenario_name):
        with goal(i.add(g.user_session.user).as_admin_to_the(r.demo_organization)):

            # add user to the demo organization
            with the(g.frontend).calls_the(g.add_user_to_demo_organization_api_view):

                # create demo organization
                with it().calls_the(g.create_organization_action):
                    with it().creates_the(r.demo_organization):
                        assert r.demo_organization.name == "demo"

                # add user to organization
                with (
                    it()
                    .calls_the(g.add_user_to_organization_action)
                    .using_the(g.display_name)
                    .in_the(r.form)
                ):
                    comment(
                        "The user can choose their display name in the frontend. "
                        + "We use a fake email address based on the display name."
                    )
                    with it().creates_the(r.demo_organization_membership):
                        assert r.demo_organization_membership.display_name
                        assert (
                            r.demo_organization_membership.member_email
                            == r.demo_organization_membership.display_name
                            + "@demo-org.com"
                        )

                # update checklist
                with it().calls_the(g.update_checklist_item_action):
                    with it().finds_the(r.join_demo_org_checklist_item).for_the(r.user):
                        assert r.join_demo_org_checklist_item

                    with it().marks_the(r.join_demo_org_checklist_item).as_completed():
                        assert r.join_demo_org_checklist_item.is_completed

    return get_scenario(scenario_name)


def run():
    from ..mrd2_a_user_creates_an_org_and_invites_a_user import (
        scenario as mrd2_scenario,
    )

    run_scenario(mrd2_scenario)
    assert g.user_session.user

    return start()


if __name__ == "__main__":
    run()
