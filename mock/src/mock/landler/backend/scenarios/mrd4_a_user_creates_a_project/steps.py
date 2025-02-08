import mock.landler.backend.namespace as B
from sunya import R as r, G as g, match_step as match, it


def implement_step(step):
    if match(
        step,
        it()
        .calls_the(g.set_active_organization_action)
        .to_set_the_active_organization_to_the(r.demo_organization),
    ):
        g.user_session.active_organization = r.demo_organization

    elif match(step, it().creates_the(r.project)):
        r.project = B.Projects.Models.Project(
            name="my-project",
        )
        r.project.plot_lists.append(
            B.PlotLists.Models.PlotList(
                name="Default Plot List", project=r.project, plots=[]
            )
        )

    elif match(step, it().creates_the(r.project_membership)):
        r.project_membership = B.Projects.Models.ProjectMembership(
            role="admin",
            project=r.project,
            organization=g.user_session.active_organization,
        )
        r.project.memberships.append(r.project_membership)
