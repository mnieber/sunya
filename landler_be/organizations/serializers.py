from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from organizations.actions.add_user_to_organization import AddUserToOrganizationForm
from organizations.actions.create_organization import CreateOrganizationForm
from organizations.models import Organization, OrganizationMembership


class CreateOrganizationFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateOrganizationForm


class AddUserToOrganizationFormSerializer(FormSerializer):
    class Meta:
        form_class = AddUserToOrganizationForm


class OrganizationSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name"]


class OrganizationMembershipSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = OrganizationMembership
        fields = ["id", "organization", "user", "role"]
