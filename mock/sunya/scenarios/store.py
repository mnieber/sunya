import typing as T

from dataclassy import dataclass
from sunya import get_actor_str
from sunya.entities import Entity
from sunya.scenarios.scenario import Scenario
from sunya.scenarios.node import Node, Step, Goal
from sunya.scenarios.preregistered_entity import PreregisteredEntity
from sunya.scenarios.memo import create_memo


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

    @classmethod
    def enter(cls, node):
        return store.stack.append(node)

    @classmethod
    def exit(cls):
        node = store.stack.pop()
        finalize_node(node)

    def __enter__(self):
        return self.enter(self.node)

    def __exit__(self, *args):
        self.exit()


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
    node = add_node(create_step(fact_bits))
    return NodeContext(node)


def create_step(fact_bits):
    return Step(fact=fact_bits, nodes=[], level=store.node.level + 1)


def add_goal(*fact_bits):
    node = add_node(create_goal(fact_bits))
    return NodeContext(node)


def create_goal(fact_bits):
    return Goal(fact=fact_bits, nodes=[], level=store.node.level + 1)


def add_node(node):
    store.node.nodes.append(node)

    for fact_bit in node.fact:
        if isinstance(fact_bit, PreregisteredEntity):
            entity = fact_bit
            if node not in entity.linked_nodes:
                entity.linked_nodes.append(node)
        if isinstance(fact_bit, Entity):
            entity = fact_bit
            node.pre_entity_memo_by_key[get_key(entity)] = create_memo(entity)

    return node


def get_key(entity):
    return (entity.__class__, get_actor_str(entity))


def get_entity(entity_class, default="__not_set__", **kwargs):
    for scenario in reversed(store.scenarios):
        if entity := scenario.get_entity(entity_class, **kwargs):
            return entity

    if default != "__not_set__":
        return default

    raise ValueError(f"Entity {entity_class} not found with {kwargs}")


def finalize_node(node):
    for entity in node.entities:
        key = get_key(entity)
        node.post_entity_memo_by_key[key] = create_memo(entity)
    node.is_finalized = True
