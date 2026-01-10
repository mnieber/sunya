# Module: projects

## Projects

```python
class Projects(DjangoModule):
    class Models:
        class Project(NowMixin):
            name: str
            memberships: RelatedSet['Projects.Models.ProjectMembership'] = []

        class ProjectMembership(Entity):
            role: 'Projects.Enums.OrganizationInProjectRoles'
            project: FK['Projects.Models.Project']
            organization: FK[Organizations.Models.Organization]

    class Forms:
        class AddOrganizationToProjectForm:
            role: 'Projects.Enums.OrganizationInProjectRoles'

    class Actions:
        class AddPlotToProject(Action):
            class Args:
                project: 'Projects.Models.Project'
                plot: 'Plots.Models.Plot'
                plot_list_name: T.Optional[str] = None

    class Enums:
        class OrganizationInProjectRoles(Enum):
            ADMIN: Any = 'admin'
            EDITOR: Any = 'editor'
            LAND_STEWARD: Any = 'land_steward'
            BUYER: Any = 'buyer'

    class DomainEvents:
        class ProjectCreated:
            pass

        class OrganizationAddedToProject:
            pass
```

