from scenarios.models import Scenario
from dataclassy import dataclass
from projects.models import Project


@dataclass
class CreateScenarioForm:
    name: str
    order: int


def create_scenario(create_scenario_form: CreateScenarioForm, project: Project):
    _validate_args(create_scenario_form, project)

    scenario = Scenario(
        name=create_scenario_form.name,
        order=create_scenario_form.order,
        project=project,
    )
    scenario.save()

    return scenario


def _validate_args(create_scenario_form: CreateScenarioForm, project: Project):
    if Scenario.objects.filter(
        name=create_scenario_form.name, project=project
    ).exists():
        raise ScenarioWithNameAlreadyExistsError()


class ScenarioWithNameAlreadyExistsError(Exception):
    pass
