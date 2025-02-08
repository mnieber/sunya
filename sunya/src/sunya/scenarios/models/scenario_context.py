from dataclassy import dataclass
import typing as T

_scenario_context = None


@dataclass
class ScenarioContext:
    resolve_entity_in_global_namespace: T.List[callable] = []
    implement_step: callable = lambda fact: None


def get_scenario_context():
    global _scenario_context

    if not _scenario_context:
        _scenario_context = ScenarioContext()
    return _scenario_context
