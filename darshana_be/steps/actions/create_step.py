import typing as T
from dataclassy import dataclass, asdict
from steps.models import Step, FactBit
from scenarios.models import Scenario


@dataclass
class CreateStepForm:
    fact: T.List[FactBit]
    parent_step: T.Optional[Step] = None
    field_delta_set_by_actor_key: T.Optional[T.Dict[str, T.Dict[str, T.Any]]] = None
    pre_actor_key_by_role_name: T.Optional[T.Dict[str, str]] = None
    post_actor_key_by_role_name: T.Optional[T.Dict[str, str]] = None


def create_step(create_step_form: CreateStepForm, scenario: Scenario) -> Step:
    _validate_args(create_step_form)

    step = Step(
        fact_json=[asdict(fb) for fb in create_step_form.fact],
        parent_step=create_step_form.parent_step,
        field_delta_set_by_actor_key=create_step_form.field_delta_set_by_actor_key
        or {},
        pre_actor_key_by_role_name=create_step_form.pre_actor_key_by_role_name or {},
        post_actor_key_by_role_name=create_step_form.post_actor_key_by_role_name or {},
        scenario=scenario,
    )
    step.save()

    return step


def _validate_args(create_step_form: CreateStepForm):
    if not create_step_form.fact:
        raise AtLeastOneFactBitIsRequiredError()


class AtLeastOneFactBitIsRequiredError(Exception):
    pass
