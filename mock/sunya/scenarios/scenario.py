import typing as T

from dataclassy import dataclass
from sunya.entities import Entity
from sunya.scenarios.step import Step


@dataclass(kw_only=True)
class Scenario:
    name: str
    entity_by_key: T.Dict[T.Tuple, Entity] = {}
    root_step: Step

    def get_entity(self, entity_class, **kwargs):
        for entity in self.entity_by_key.values():
            if isinstance(entity, entity_class):
                found = True
                for key, value in kwargs.items():
                    if getattr(entity, key) != value:
                        found = False
                        break
                if found:
                    return entity
        return None

    def get_list_of_steps(self, step=None):
        result = [step] if step else []
        source_step = step or self.root_step
        for child_step in source_step.steps:
            for s in self.get_list_of_steps(child_step):
                result.append(s)

        return result
