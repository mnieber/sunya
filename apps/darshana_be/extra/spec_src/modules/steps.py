from mock.default.stack.namespace import Module, Form
from mock.default.backend.namespace import Action
import typing as T

from sunya import EntityWithId


class Steps(Module):
    class Models:
        class FactBit(EntityWithId):
            type_name: str = "FactBitTypeNames: string | role | actor"
            value: str

        class Step(EntityWithId):
            fact: T.Tuple["Steps.Models.FactBit"]
            parent_step: T.Optional["Steps.Models.Step"] = None
            child_steps: T.List["Steps.Models.Step"] = []
            field_delta_set_by_actor_key: T.Dict[str, T.Dict[str, T.Any]] = {}

    class Actions:
        class CreateStep(Action):
            class Args:
                create_step_form: Form
                parent_step: T.Optional["Steps.Models.Step"]

    class DomainEvents:
        pass
