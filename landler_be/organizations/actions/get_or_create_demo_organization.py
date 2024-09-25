from organizations.actions.create_organization import (
    CreateOrganizationForm,
    create_organization,
)
from organizations.models import Organization


def get_or_create_demo_organization():
    demo_org = Organization.objects.filter(name="Demo Organization").first()
    if demo_org:
        return demo_org

    demo_org = create_organization(CreateOrganizationForm(name="Demo Organization"))
    demo_org.staff_settings.is_demo_org = True
    demo_org.staff_settings.save()
    return demo_org
