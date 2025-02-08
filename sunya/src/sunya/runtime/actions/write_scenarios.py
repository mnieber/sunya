from sunya.runtime.rules.get_scenario_description import get_scenario_description
from sunya.scenarios.models.scenario_context import get_scenario_context
from sunya.runtime.utils.get_scenario_path import get_scenario_path
from sunya.runtime.actions.run_scenario import run_scenario
from sunya.utils.yaml import dict2yaml


def write_scenarios(config, scenario_names, file_writer):
    get_scenario_context().resolve_entity_in_global_namespace = config[
        "resolve_entity_in_global_namespace"
    ]
    for idx, scenario_name in enumerate(scenario_names):
        layer, scenario_path = get_scenario_path(config, scenario_name)
        scenario = run_scenario(scenario_path)
        scenario_yaml = dict2yaml(get_scenario_description(scenario, idx))
        file_writer.write_scenario(scenario_name, scenario_yaml)
