import factory
from projects.models import Project
from factory.django import DjangoModelFactory


class ProjectFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Project{n}")
    description = "Some project description"

    class Meta:
        model = Project
