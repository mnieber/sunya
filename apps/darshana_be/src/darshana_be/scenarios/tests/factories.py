import factory
from darshana_be.scenarios.models import Scenario
from factory.django import DjangoModelFactory
from darshana_be.projects.tests.factories import ProjectFactory


class ScenarioFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Scenario{n}")
    project = factory.SubFactory(ProjectFactory)

    class Meta:
        model = Scenario

    @factory.post_generation
    def root_step(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.root_step = extracted
            self.save()
