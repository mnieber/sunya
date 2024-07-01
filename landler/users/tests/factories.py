import factory
from factory.django import DjangoModelFactory

from users.models import User


class UserFactory(DjangoModelFactory):
    email = factory.Sequence(lambda n: f"User{n}")

    class Meta:
        model = User
