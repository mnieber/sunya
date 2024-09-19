import typing as T
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
from actors.actions.create_role import create_role, CreateRoleForm


@dataclass
class ImportScenarioSpecForm:
    scenario_data: T.Dict[str, T.Any]


def import_scenario_spec(
    import_scenario_spec_form: ImportScenarioSpecForm, project: Project
):
    #
    _validate_args(import_scenario_spec_form)

    data = import_scenario_spec_form.scenario_data

    with transaction.atomic():
        scenario = create_scenario(
            CreateScenarioForm(name=data["scenario_name"]), project
        )
        steps = _process_nodes(data["nodes"], scenario)

        scenario.root_step = steps[0]
        scenario.save()

    return scenario


def _validate_args(import_scenario_spec_form: ImportScenarioSpecForm):
    root_nodes = import_scenario_spec_form.scenario_data.get("nodes", [])
    if len(root_nodes) != 1:
        raise NotExactlyOneRootNodeError()


def _process_nodes(
    nodes: T.List[dict], scenario: Scenario, parent_step: T.Optional[Step] = None
):
    steps = []
    for node in nodes:
        if "goal" in node:
            step = _create_step(node["goal"], scenario, parent_step)
        elif "step" in node:
            step = _create_step(node["step"], scenario, parent_step)
        else:
            if parent_step:
                raise InvalidNodeError(node)
            step = _create_step("root", scenario, parent_step)

        steps.append(step)
        _process_actors_introduced(node.get("actors_introduced", []), step)
        _process_roles(node.get("pre_actor_key_by_role_name", {}), step)
        _process_roles(node.get("post_actor_key_by_role_name", {}), step)
        if "child_nodes" in node:
            _process_nodes(node["child_nodes"], scenario, step)

    return steps


def _create_step(
    fact_str: str, scenario: Scenario, parent_step: T.Optional[Step] = None
) -> Step:
    fact_bits = _parse_fact_string(fact_str)
    create_step_form = CreateStepForm(
        fact=fact_bits, parent_step=parent_step, field_delta_set_by_actor_key={}
    )

    step = create_step(create_step_form, scenario)

    for fact_bit in step.fact:
        if fact_bit.type_name == FactBitTypeNames.ACTOR.value:
            _get_or_create_actor(fact_bit.value)
        if fact_bit.type_name == FactBitTypeNames.ROLE.value:
            _get_or_create_role(fact_bit.value)

    return step


def _parse_fact_string(fact_str: str) -> T.List[FactBit]:
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


def _process_actors_introduced(actors_introduced: T.List[dict], step: Step):
    for actor in actors_introduced:
        actor_key = actor["name"]
        deltas = actor.get("deltas", {})
        step.field_delta_set_by_actor_key[actor_key] = deltas

    step.save()


def _process_roles(actor_key_by_role_name: dict, step: Step):
    for role_name, actor_key in actor_key_by_role_name.items():
        _get_or_create_actor(actor_key)


def _get_or_create_actor(actor_key: str) -> Actor:
    actor = Actor.objects.filter(key=actor_key).first()
    if not actor:
        actor = create_actor(CreateActorForm(key=actor_key))
    return actor


def _get_or_create_role(role_name: str) -> Role:
    role = Role.objects.filter(name=role_name).first()
    if not role:
        role = create_role(CreateRoleForm(name=role_name))
    return role


class NotExactlyOneRootNodeError(Exception):
    pass


class InvalidNodeError(ValueError):
    pass
