import importlib

from sunya.runtime.rules.get_scenario_markdown import get_scenario_markdown
from sunya.runtime.utils.get_scenario_module_path import get_scenario_module_path
from sunya.scenarios.models.scenario import get_scenario


def write_scenarios(config, scenario_names, file_writer):
    for scenario_name in scenario_names:
        layer, scenario_module_path = get_scenario_module_path(config, scenario_name)
        importlib.import_module(f"{scenario_module_path}")
        scenario = get_scenario()
        scenario_markdown = get_scenario_markdown(scenario)
        file_writer.write_scenario(scenario, scenario_markdown)
