import factory
from darshana_be.actors.models import Actor, Role
from factory.django import DjangoModelFactory


class ActorFactory(DjangoModelFactory):
    key = factory.Sequence(lambda n: f"actor{n}")

    class Meta:
        model = Actor


class RoleFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"role{n}")

    class Meta:
        model = Role
