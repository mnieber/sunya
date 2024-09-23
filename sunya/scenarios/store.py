import typing as T
import os

from dataclassy import dataclass
from sunya import get_actor_str
from sunya.entities import Entity
from sunya.scenarios.scenario import Scenario
from sunya.scenarios.node import Goal, Node, Step
from sunya.scenarios.memo import create_memo
from sunya.scenarios.roles import Role


@dataclass(kw_only=True)
class Store:
    scenarios: T.List[Scenario] = []
    stack: T.List = []
    roles: T.List = []

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
    scenario = Scenario(name=name)
    store.scenarios.append(scenario)

    return NodeContext(scenario.root_node)


def get_scenario(name: str):
    for scenario in store.scenarios:
        if scenario.name == name:
            return scenario
    return None


def get_scenario_name(file_path):
    return os.path.basename(file_path).replace(".py", "")


def create_goal(fact_bits):
    return Goal(
        scenario=store.scenario, fact=fact_bits, nodes=[], level=store.node.level + 1
    )


def create_step(fact_bits):
    return Step(
        scenario=store.scenario, fact=fact_bits, nodes=[], level=store.node.level + 1
    )


def add_step(*fact_bits):
    node = add_node(create_step(fact_bits))
    return NodeContext(node)


def add_goal(*fact_bits):
    node = add_node(create_goal(fact_bits))
    return NodeContext(node)


def add_node(node):
    store.node.nodes.append(node)

    for fact_bit in node.fact:
        if isinstance(fact_bit, Role):
            role = fact_bit
            entity = role.actor
            if entity:
                node.pre_actor_key_by_role_name[role.name] = get_key(entity)
        elif isinstance(fact_bit, Entity):
            entity = fact_bit
        else:
            entity = None

        if entity:
            node.pre_entity_memo_by_key[get_key(entity)] = create_memo(entity)

    return node


def get_key(entity):
    return (entity.__class__, get_actor_str(entity))


def finalize_node(node):
    for fact_bit in node.fact:
        entity = None
        role = None

        if isinstance(fact_bit, Entity):
            entity = fact_bit
        elif isinstance(fact_bit, Role):
            role = fact_bit
            entity = role.actor
        else:
            continue

        if entity:
            key = get_key(entity)
            node.post_entity_memo_by_key[key] = create_memo(entity)
            if role:
                node.post_actor_key_by_role_name[role.name] = key

    node.is_finalized = True
