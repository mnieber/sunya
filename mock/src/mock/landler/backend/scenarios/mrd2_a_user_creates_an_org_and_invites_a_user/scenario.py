from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    it,
    the,
    G as g,
    R as r,
    I as i,
)

scenario_name = f"backend/mrd2_a_user_creates_an_org_and_invites_a_user"


def start():
    with add_scenario(scenario_name):
        with goal(i.create_an(r.organization).with_admin(g.user_session.user)):

            # create an organization for the user
            with the(g.frontend).calls_the(g.create_organization_api_view):

                # create organization
                with it().calls_the(g.create_organization_action):
                    with it().creates_the(r.organization):
                        assert r.organization.name == "my-org"

                    # add user to organization
                    with it().calls_the(g.add_user_to_organization_action):
                        with it().creates_the(r.organization_membership):
                            assert r.organization_membership

                # find checklist item
                with it().finds_the(r.create_org_checklist_item).for_the(r.user):
                    pass

                # update checklist item
                with it().calls_the(g.update_checklist_item_action):
                    with it().marks_the(r.create_org_checklist_item).as_completed():
                        pass

        # set organization as the active organization
        with the(r.user).uses_the(g.organization_picker).in_the(
            g.frontend
        ).to_switch_to_the(g.organization_route).of_the(r.organization):
            with the(r.user).is_redirected_to_the(g.organization_route):
                pass

            with goal(i.set(r.organization).as_the_active_organization()):
                with the(g.frontend).calls_the(g.set_active_organization_api_view):
                    with it().calls_the(g.set_active_organization_action):
                        with it().sets(
                            r.organization
                        ).as_the_active_organization_in_the(g.user_session):
                            pass

    return get_scenario(scenario_name)


def run():
    from ..mrd1_a_user_signs_up_and_sees_a_checklist import scenario as mrd1_scenario

    run_scenario(mrd1_scenario)
    assert g.user_session.user == r.user

    return start()


if __name__ == "__main__":
    run()
