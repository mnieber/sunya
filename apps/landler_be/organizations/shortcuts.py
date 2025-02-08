from rest_framework.exceptions import ValidationError

from organizations.models import Organization


def get_organization_or_400(organization_id):
    organization = Organization.objects.filter(pk=organization_id).first()
    if not organization:
        raise ValidationError(code="ORGANIZATION_NOT_FOUND")
    return organization
