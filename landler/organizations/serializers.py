from organizations.actions.create_organization import CreateOrganizationForm
from organizations.models import Organization

from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadOnlySerializerMixin


class CreateOrganizationFormSerializer(FormSerializer):
    class Meta:
        model = CreateOrganizationForm


class OrganizationSerializer(ReadOnlySerializerMixin, BaseModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
