from default.stack.namespace import Module
from default.frontend.entities import Component
from sunya import G as g


class Organizations(Module):
    class Types:
        class Organization:
            name: str
            staff_settings: "Organizations.Types.OrganizationStaffSettings"

        class OrganizationStaffSettings:
            is_demo_org: bool

    class Components:
        class OrganizationPicker(Component):
            pass


g.organization_picker = Organizations.Components.OrganizationPicker()
