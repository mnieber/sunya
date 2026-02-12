from dataclassy import asdict
import factory
from darshana_be.steps.models import Step, FactBit
from factory.django import DjangoModelFactory
from darshana_be.scenarios.tests.factories import ScenarioFactory
from darshana_be.steps.enums import FactBitTypeNames
from darshana_be.common.utils.test_utils import fake


def generate_factbit_value(factbit):
    if factbit.type_name == FactBitTypeNames.STRING.value:
        return fake("sentence")
    elif factbit.type_name == FactBitTypeNames.ROLE.value:
        return fake("word").title()
    elif factbit.type_name == FactBitTypeNames.ACTOR.value:
        return f"{fake('word')}:{fake('word')}"
    else:
        raise ValueError(f"Invalid FactBit type: {factbit.type_name}")


class FactBitFactory(factory.Factory):
    class Meta:
        model = FactBit

    type_name = factory.Iterator([t.value for t in FactBitTypeNames])
    value = factory.LazyAttribute(generate_factbit_value)


class StepFactory(DjangoModelFactory):
    class Meta:
        model = Step

    scenario = factory.SubFactory(ScenarioFactory)
    fact_json = factory.LazyFunction(lambda: [asdict(FactBitFactory())])
    field_delta_set_by_actor_key = factory.Dict({})

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        return super()._create(model_class, *args, **kwargs)
