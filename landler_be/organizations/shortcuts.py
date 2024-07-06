from rest_framework.generics import get_object_or_404

from organizations.models import Organization


def get_organization_or_404(organization_id):
    return get_object_or_404(Organization, pk=organization_id)
