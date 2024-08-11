import copy
import typing as T

from dataclassy import Internal, dataclass
from sunya import get_actor_str
from sunya.entities import Entity
from sunya.scenarios.scenario import Scenario, Step, Goal


@dataclass(kw_only=True)
class Store:
    scenarios: T.List[Scenario] = []
    stack: T.List = []

    @property
    def scenario(self):
        return self.scenarios[-1]

    @property
    def node(self):
        return self.stack[-1]


class NodeContext:
    def __init__(self, node: Node):
        self.node = node

    def __enter__(self):
        store.stack.append(self.node)

    def __exit__(self, *args):
        node = store.stack.pop()
        finalize_node(node)


@dataclass(kw_only=True)
class PreregisteredEntity:
    key: str
    linked_nodes: Internal[T.List[Node]] = []


store = Store()


def add_scenario(name: str):
    scenario = Scenario(name=name, root_node=Node(fact=tuple(), level=0))
    store.scenarios.append(scenario)

    return NodeContext(scenario.root_node)


def get_scenario(name: str):
    for scenario in store.scenarios:
        if scenario.name == name:
            return scenario
    return None


def add_step(*fact_bits):
    return _add_node(Step, *fact_bits)


def add_goal(*fact_bits):
    return _add_node(Goal, *fact_bits)


def _add_node(klass, *fact_bits):
    node = klass(fact=fact_bits, nodes=[], level=store.node.level + 1)
    store.node.nodes.append(node)

    for fact_bit in fact_bits:
        if isinstance(fact_bit, PreregisteredEntity):
            entity = fact_bit
            if node not in entity.linked_nodes:
                entity.linked_nodes.append(node)
        if isinstance(fact_bit, Entity):
            entity = fact_bit
            register(entity)
            node.pre_entity_memo_by_key[get_key(entity)] = create_memo(entity)

    return NodeContext(node)


def register(entity, preregistered_entity=None, name=None, force=False):
    key = get_key(entity)
    if key in store.scenario.entity_by_key:
        existing_entity = store.scenario.entity_by_key[key]
        if existing_entity is not entity:
            raise ValueError(
                f"Entity {existing_entity} already registered under key {key}"
            )

    store.scenario.entity_by_key[key] = entity

    if name:
        if name in store.scenario.entity_by_name and not force:
            raise ValueError(f"Entity with name {name} already exists")
        store.scenario.entity_by_name[name] = entity

    if preregistered_entity:
        # Register the fact that before this node, the entity did not yet exist
        for linked_node in preregistered_entity.linked_nodes:
            linked_node.pre_entity_memo_by_key[key] = None

            # Update node.fact to replace preregistered_entity with entity
            linked_node.fact = tuple(
                entity if fact_bit is preregistered_entity else fact_bit
                for fact_bit in linked_node.fact
            )

    return entity


def get_key(entity):
    return (entity.__class__, get_actor_str(entity))


def get_entity(entity_class, default="__not_set__", **kwargs):
    for scenario in reversed(store.scenarios):
        if entity := scenario.get_entity(entity_class, **kwargs):
            return entity

    if default != "__not_set__":
        return default

    raise ValueError(f"Entity {entity_class} not found with {kwargs}")


def preregister(key: str):
    return PreregisteredEntity(key=key)


def finalize_node(node):
    for entity in node.entities:
        key = get_key(entity)
        node.post_entity_memo_by_key[key] = create_memo(entity)
    node.is_finalized = True


class NoValue:
    pass


def get_entity_delta(node, entity):
    if not node.is_finalized:
        raise NodeNotFinalizedError(node)

    key = get_key(entity)
    pre_entity_memo = node.pre_entity_memo_by_key.get(key)
    post_entity_memo = node.post_entity_memo_by_key.get(key)

    delta = dict()
    for field, value in (post_entity_memo or dict()).items():
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
    return get_actor_str(x) if isinstance(x, Entity) else copy.deepcopy(x)


class NodeNotFinalizedError(Exception):
    def __init__(self, node):
        self.node = node
        super().__init__(f"Node {node} has not been finalized")


class EntityLookup:
    def __getattr__(self, name):
        for scenario in reversed(store.scenarios):
            if entity := scenario.get_entity_by_name(name):
                return entity

        raise ValueError(f"Entity with name {name} not found")


def get_entities():
    return EntityLookup()
