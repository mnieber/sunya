import factory
from factory.django import DjangoModelFactory

from organizations.enums import UserInOrganizationRoles
from organizations.models import Organization, OrganizationMembership
from users.tests.factories import UserFactory


class OrganizationFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Organization {n}")

    class Meta:
        model = Organization


class OrganizationMembershipFactory(DjangoModelFactory):
    organization = factory.SubFactory(OrganizationFactory)
    user = factory.SubFactory(UserFactory)
    role = UserInOrganizationRoles.EDITOR

    class Meta:
        model = OrganizationMembership
