from kits.react_app.impl.namespace import Component, ReactModule
from sunya import FK


class Organizations(ReactModule):
    class Types:
        class Organization:
            name: str
            staff_settings: FK["Organizations.Types.OrganizationStaffSettings"]

        class OrganizationStaffSettings:
            is_demo_org: bool

    class Components:
        class OrganizationPicker(Component):
            pass
