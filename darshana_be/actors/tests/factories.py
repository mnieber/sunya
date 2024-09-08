import factory
from actors.models import Actor
from factory.django import DjangoModelFactory


class ActorFactory(DjangoModelFactory):
    key = factory.Sequence(lambda n: f"actor{n}")

    class Meta:
        model = Actor
