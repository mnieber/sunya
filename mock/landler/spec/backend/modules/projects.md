1 Models

1.1 Model: Project

name: str
memberships: list[ProjectMembership]

1.2 Model: ProjectMembership

project: Project
organization: Organization
role: OrganizationInProjectRoles

2 Enums

2.1 Enum: OrganizationInProjectRoles

Items:
admin
editor
land_steward
buyer

3 Actions

3.1 Action: create_project

Arguments:
create_project_form: Form

3.2 Action: add_organization_to_project

Arguments:
project: Project
organization: Organization
role: OrganizationInProjectRoles

3.3 Action: add_plot_to_project

Arguments:
project: Project
plot: Plot

4 Api views

