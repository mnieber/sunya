import factory
from steps.models import Step
from factory.django import DjangoModelFactory
import json
from scenarios.tests.factories import ScenarioFactory
from steps.enums import FactBitTypeNames


class StepFactory(DjangoModelFactory):
    scenario = factory.SubFactory(ScenarioFactory)
    fact = factory.LazyFunction(
        lambda: json.dumps(
            [{"type_name": FactBitTypeNames.STRING.value, "value": "Test step"}]
        )
    )
    field_delta_set_by_actor_key = factory.Dict({})

    class Meta:
        model = Step
