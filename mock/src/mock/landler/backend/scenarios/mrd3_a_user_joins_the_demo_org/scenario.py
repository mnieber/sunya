from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
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
                with (
                    it()
                    .finds_the(r.demo_organization)
                    .and_if_not_found_it()
                    .calls_the(g.create_organization_action)
                ):
                    with it().creates_the(r.demo_organization):
                        assert r.demo_organization.name == "demo"

                # add user to organization
                with (
                    it()
                    .calls_the(g.add_user_to_organization_action)
                    .using_the(g.display_name)
                    .found_in_the(r.form)
                ):
                    """
                    The user can choose their display name in the frontend.
                    We use a fake email address based on the display name.
                    """
                    with it().creates_the(r.demo_organization_membership):
                        assert r.demo_organization_membership.display_name
                        assert (
                            r.demo_organization_membership.member_email
                            == r.demo_organization_membership.display_name
                            + "@demo-org.com"
                        )

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


from sunya import G as m
from sunya import G as r
from sunya import G as goals

diagram = f"""
```mermaid
sequenceDiagram
    participant {m.External.Frontend}
    participant {m.Organizations.AddUserToDemoOrganizationAPIView}
    participant {m.Organizations.Actions.AddUserToDemoOrganization}
    participant {m.Organizations.Rules.CreateRandomDisplayName}
    participant {m.Organizations.Actions.CreateOrganization}
    participant {m.Organizations.Actions.AddUserToOrganization}

    # 🔳 Add user to demo org
    {goals.note_over(r.Frontend, goal().add_the(r.user).to_the(r.demo_organization))}
    {r.Frontend                         >> r.AddUserToDemoOrganizationAPIView}  : {g.calls(r.current_user)}
    {r.AddUserToDemoOrganizationAPIView >> r.AddUserToDemoOrganization}         : {g.calls(r.current_user)}
    {r.AddUserToDemoOrganization        >> r.self}                              : {g.finds_the(r.demo_organization)}
    alt organization not found
        {r.AddUserToDemoOrganization >> r.CreateOrganization} : {g.calls(r.create_organization_form)}
        {r.CreateOrganization        >> r.self}               : {g.creates(r.demo_organization)}
    end
    {r.AddUserToDemoOrganization >> r.CreateRandomDisplayName} : {g.calls()}
    {r.AddUserToDemoOrganization >> r.AddUserToOrganization}   : {g.calls(r.demo_organization, r.current_user, r.add_user_to_organization_form)}
    {r.AddUserToOrganization     >> r.self}                    : {g.creates(r.demo_organization_membership)}

```