import typing as T
from dataclassy import asdict, dataclass
from steps.models import Step, FactBit
from django.core.exceptions import ValidationError
import json
from steps.enums import FactBitTypeNames
from scenarios.models import Scenario


@dataclass
class CreateStepForm:
    fact: T.List[FactBit]
    parent_step: T.Optional[Step] = None
    field_delta_set_by_actor_key: T.Dict[str, T.Dict[str, T.Any]] = None


def create_step(create_step_form: CreateStepForm, scenario: Scenario) -> Step:
    _validate_args(create_step_form)

    step = Step(
        fact=json.dumps([asdict(fb) for fb in create_step_form.fact]),
        scenario=scenario,
        parent_step=create_step_form.parent_step,
        field_delta_set_by_actor_key=create_step_form.field_delta_set_by_actor_key
        or {},
    )
    step.save()

    return step


def _validate_args(create_step_form: CreateStepForm):
    if not create_step_form.fact:
        raise AtLeastOneFactBitIsRequiredError()

    for fact_bit in create_step_form.fact:
        if fact_bit.type_name not in [member.value for member in FactBitTypeNames]:
            raise InvalidFactBitTypeValidationError(fact_bit.type_name)


class AtLeastOneFactBitIsRequiredError(Exception):
    pass


class InvalidFactBitTypeValidationError(ValidationError):
    def __init__(self, type_name):
        super().__init__(f"Invalid FactBit type: {type_name}")
