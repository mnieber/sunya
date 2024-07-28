from landler.stack.entities import Module
from blogs.frontend.entities import Route, Component


class Organizations(Module):
    class Routes:
        class OrganizationRoute(Route):
            pass

    class Components:
        class OrganizationPicker(Component):
            pass


organization_route = Organizations.Routes.OrganizationRoute()
organization_picker = Organizations.Components.OrganizationPicker()
