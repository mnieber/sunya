import factory
from factory.django import DjangoModelFactory
from organizations.models import Organization


class OrganizationFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Organization{n}")

    class Meta:
        model = Organization
