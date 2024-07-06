import copy
import typing as T

from dataclassy import Internal, dataclass
from sunya import actor_to_str
from sunya.entities import Entity
from sunya.entities.get_actor_key import get_actor_key
from sunya.scenarios.scenario import Scenario, Step


@dataclass(kw_only=True)
class Store:
    scenarios: T.List[Scenario] = []
    stack: T.List = []

    @property
    def scenario(self):
        return self.scenarios[-1]

    @property
    def step(self):
        return self.stack[-1]


class StepContext:
    def __init__(self, step: Step):
        self.step = step

    def __enter__(self):
        store.stack.append(self.step)

    def __exit__(self, *args):
        step = store.stack.pop()
        finalize_step(step)


@dataclass(kw_only=True)
class PreregisteredEntity:
    key: str
    linked_steps: Internal[T.List[Step]] = []


store = Store()


def add_scenario(name: str):
    scenario = Scenario(name=name, root_step=Step(fact=tuple(), level=0))
    store.scenarios.append(scenario)

    return StepContext(scenario.root_step)


def get_scenario(name: str):
    for scenario in store.scenarios:
        if scenario.name == name:
            return scenario
    return None


def add_step(*fact_bits):
    step = Step(fact=fact_bits, steps=[], level=store.step.level + 1)
    store.step.steps.append(step)

    for fact_bit in fact_bits:
        if isinstance(fact_bit, PreregisteredEntity):
            entity = fact_bit
            if step not in entity.linked_steps:
                entity.linked_steps.append(step)
        if isinstance(fact_bit, Entity):
            entity = fact_bit
            register(entity)
            step.pre_entity_memo_by_key[get_key(entity)] = create_memo(entity)

    return StepContext(step)


def register(entity, preregistered_entity=None, name=None):
    key = get_key(entity)
    if key in store.scenario.entity_by_key:
        existing_entity = store.scenario.entity_by_key[key]
        if existing_entity is not entity:
            raise ValueError(
                f"Entity {existing_entity} already registered under key {key}"
            )

    store.scenario.entity_by_key[key] = entity

    if preregistered_entity:
        # Register the fact that before this step, the entity did not yet exist
        for linked_step in preregistered_entity.linked_steps:
            linked_step.pre_entity_memo_by_key[key] = None

            # Update step.fact to replace preregistered_entity with entity
            linked_step.fact = tuple(
                entity if fact_bit is preregistered_entity else fact_bit
                for fact_bit in linked_step.fact
            )

    return entity


def get_key(entity):
    return (entity.__class__, get_actor_key(entity))


def get_entity(entity_class, default="__not_set__", **kwargs):
    for scenario in reversed(store.scenarios):
        if entity := scenario.get_entity(entity_class, **kwargs):
            return entity

    if default != "__not_set__":
        return default

    raise ValueError(f"Entity {entity_class} not found with {kwargs}")


def preregister(key: str):
    return PreregisteredEntity(key=key)


def finalize_step(step):
    for entity in step.entities:
        key = get_key(entity)
        step.post_entity_memo_by_key[key] = create_memo(entity)


class NoValue:
    pass


def get_entity_delta(step, entity):
    key = get_key(entity)
    pre_entity_memo = step.pre_entity_memo_by_key.get(key)
    post_entity_memo = step.post_entity_memo_by_key.get(key)

    delta = dict()
    for field, value in post_entity_memo.items():
        existing_value = (
            pre_entity_memo.get(field, NoValue) if pre_entity_memo else NoValue
        )
        delta[field] = (existing_value, value)
    return delta


def _iter_fields(obj):
    for name in dir(obj):
        if not name.startswith("__"):
            yield name, getattr(obj, name)


def create_memo(entity):
    memo = {}
    for field, value in _iter_fields(entity):
        if isinstance(value, list):
            memo_value = [_get_memo_field_value(x) for x in value]
        elif isinstance(value, dict):
            memo_value = {k: _get_memo_field_value(v) for k, v in value.items()}
        else:
            memo_value = _get_memo_field_value(value)

        memo[field] = memo_value
    return memo


def _get_memo_field_value(x):
    return actor_to_str(x) if isinstance(x, Entity) else copy.deepcopy(x)
