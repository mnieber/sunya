from typing import Any, Dict, List
from dataclassy import dataclass

from django.db import transaction
from projects.models import Project
from scenarios.models import Scenario
from scenarios.actions.create_scenario import create_scenario, CreateScenarioForm
from steps.models import Step, FactBit
from steps.actions.create_step import create_step, CreateStepForm
from actors.models import Actor, Role
from actors.actions.create_actor import create_actor, CreateActorForm
from steps.enums import FactBitTypeNames


@dataclass
class ImportScenarioSpecForm:
    scenario_data: Dict[str, Any]


def import_scenario_spec(
    import_scenario_spec_form: ImportScenarioSpecForm, project: Project
):
    data = import_scenario_spec_form.scenario_data

    with transaction.atomic():
        scenario = create_scenario(
            CreateScenarioForm(name=data["scenario_name"]), project
        )
        _process_nodes(data["nodes"], scenario)

    return scenario


def _process_nodes(nodes: List[dict], scenario: Scenario, parent_step: Step = None):
    for node in nodes:
        if "goal" in node:
            step = _create_step(node["goal"], scenario, parent_step)
            _process_actors_introduced(node.get("actors_introduced", []), step)
            _process_roles_updated(node.get("roles_updated", {}), step)
        elif "step" in node:
            step = _create_step(node["step"], scenario, parent_step)
        else:
            continue

        if "child_nodes" in node:
            _process_nodes(node["child_nodes"], scenario, step)


def _create_step(fact_str: str, scenario: Scenario, parent_step: Step = None) -> Step:
    fact_bits = _parse_fact_string(fact_str)
    create_step_form = CreateStepForm(
        fact=fact_bits, parent_step=parent_step, field_delta_set_by_actor_key={}
    )
    return create_step(create_step_form, scenario)


def _parse_fact_string(fact_str: str) -> List[FactBit]:
    fact_bits = []
    parts = fact_str.split()
    for part in parts:
        if part.startswith("[") and part.endswith("]"):
            actor_key = part[1:-1]
            if ":" in actor_key:
                fact_bits.append(
                    FactBit(type_name=FactBitTypeNames.ACTOR.value, value=actor_key)
                )
            else:
                fact_bits.append(
                    FactBit(type_name=FactBitTypeNames.ROLE.value, value=actor_key)
                )
        else:
            fact_bits.append(
                FactBit(type_name=FactBitTypeNames.STRING.value, value=part)
            )
    return fact_bits


def _process_actors_introduced(actors_introduced: List[dict], step: Step):
    for actor in actors_introduced:
        actor_key = actor["name"]
        _create_or_get_actor(actor_key)

        deltas = actor.get("deltas", {})
        step.field_delta_set_by_actor_key[actor_key] = deltas

    step.save()


def _process_roles_updated(roles_updated: dict, step: Step):
    for role_name, actor_key in roles_updated.items():
        _create_or_get_role(role_name)
        _create_or_get_actor(actor_key)

        # You might want to store this information in the step or another model
        # For now, we'll just print it
        print(f"Role {role_name} updated to {actor_key}")


def _create_or_get_actor(actor_key: str) -> Actor:
    actor, created = Actor.objects.get_or_create(key=actor_key)
    if created:
        create_actor(CreateActorForm(key=actor_key))
    return actor


def _create_or_get_role(role_name: str) -> Role:
    return Role.objects.get_or_create(name=role_name)[0]
