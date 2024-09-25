from dataclassy import dataclass
from django.contrib.auth import get_user_model

from organizations.actions.add_user_to_organization import (
    AddUserToOrganizationForm,
    add_user_to_organization,
)
from organizations.actions.get_or_create_demo_organization import (
    get_or_create_demo_organization,
)
from organizations.enums import UserInOrganizationRoles

User = get_user_model()


@dataclass
class AddUserToDemoOrganizationForm:
    display_name: str


def add_user_to_demo_organization(add_user_to_demo_organization_form, user: User):
    demo_org = get_or_create_demo_organization()

    add_user_to_organization(
        AddUserToOrganizationForm(
            role=UserInOrganizationRoles.ADMIN,
            display_name=add_user_to_demo_organization_form.display_name,
            member_email=_get_member_email(
                add_user_to_demo_organization_form.display_name
            ),
        ),
        demo_org,
        user,
    )


def _get_member_email(display_name):
    return f"{display_name.replace(' ', '').lower()}@demo-org.com"
