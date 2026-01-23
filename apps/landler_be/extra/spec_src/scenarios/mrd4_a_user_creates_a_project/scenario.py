from sunya import (
    goal,
    add_scenario,
    get_scenario,
    run_scenario,
    it,
    the,
    G as g,
    I as i,
    R as r,
)


scenario_name = f"backend/mrd4_a_user_creates_a_project"


def start():
    with add_scenario(scenario_name):
        # set demo organization as active
        with (
            the(g.frontend)
            .calls_the(g.set_active_organization_api_view)
            .to_set_the_active_organization_to_the(r.demo_organization)
        ):
            with (
                it()
                .calls_the(g.set_active_organization_action)
                .to_set_the_active_organization_to_the(r.demo_organization)
            ):
                pass

        # create a project in the demo organization
        with goal(i.create_a(r.project).with_admin(g.user_session.active_organization)):
            with the(g.frontend).calls_the(g.create_project_api_view):
                with it().calls_the(g.create_project_action):
                    with it().creates_the(r.project):
                        assert r.project.plot_lists[0].name == "Default Plot List"

                    with it().calls_the(g.add_organization_to_project_action):
                        with it().creates_the(r.project_membership):
                            assert r.project_membership.role == "admin"
                            assert (
                                r.project_membership.organization == r.demo_organization
                            )

    return get_scenario(scenario_name)


def run():
    from ..mrd3_a_user_joins_the_demo_org import scenario as mrd3_scenario

    run_scenario(mrd3_scenario)

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
    participant {m.Organizations.ApiViews.SetActiveOrganizationApiView}
    participant {m.Organizations.Actions.SetActiveOrganization}
    participant {m.Projects.ApiViews.CreateProjectApiView}
    participant {m.Projects.Actions.CreateProject}
    participant {m.Projects.Actions.AddOrganizationToProject}

    # 🔳 Set Active Organization
    {goals.note_over(r.Frontend, goal().set_the_active_organization_to_the(r.demo_organization))}
    {r.Frontend                     >> r.SetActiveOrganizationApiView} : {g.calls()}
    {r.SetActiveOrganizationApiView >> r.SetActiveOrganization}        : {g.calls(r.demo_organization)}
    {r.SetActiveOrganization        >> r.self}                         : {g.sets(r.demo_organization).as_the(r.active_organization)}

    # 🔳 Create Project
    {goals.note_over(r.Frontend, goal().create_a(r.project).in_the(r.demo_organization))}
    {r.Frontend                 >> r.CreateProjectApiView}     : {g.calls()}
    {r.CreateProjectApiView     >> r.CreateProject}            : {g.calls(r.create_project_form)}
    {r.CreateProject            >> r.self}                     : {g.creates(r.project)}
    {r.CreateProject            >> r.AddOrganizationToProject} : {g.calls(r.project, organization=r.demo_organization, add_organization_to_project_form=r.add_organization_to_project_form)}
    {r.AddOrganizationToProject >> r.self}                     : {g.creates(r.project_membership)}
    {r.AddOrganizationToProject >> r.CreateProjectApiView}     : {g.returns(r.project)}
```
"""
