import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_active = True

    class Meta:
        model = User

    @classmethod
    def create(cls, **kwargs):
        from checklists.actions.create_checklist import create_checklist

        user = super().create(**kwargs)
        create_checklist(user)
        return user


class InactiveUserFactory(UserFactory):
    is_active = False
