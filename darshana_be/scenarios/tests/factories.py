import factory
from scenarios.models import Scenario
from factory.django import DjangoModelFactory
from projects.tests.factories import ProjectFactory


class ScenarioFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Scenario{n}")
    project = factory.SubFactory(ProjectFactory)

    class Meta:
        model = Scenario

    @factory.post_generation
    def root_step(self, create, extracted, **kwargs):
        from steps.tests.factories import StepFactory

        if not create:
            return

        if extracted:
            self.root_step = extracted
            extracted.scenario = self
            extracted.save()
        else:
            self.root_step = StepFactory(scenario=self)

        self.save()
