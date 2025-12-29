import importlib

from sunya.runtime.rules.get_scenario_markdown import get_scenario_markdown
from sunya.runtime.utils.filepath_to_import_path import filepath_to_import_path
from sunya.runtime.utils.file_writer import FileWriter
from sunya.scenarios.models.scenario import get_scenario


def write_scenarios(scenario_spec_paths, file_writer: FileWriter):
    for scenario_module_path in scenario_spec_paths:
        importlib.import_module(filepath_to_import_path(scenario_module_path))
        scenario = get_scenario()
        scenario_markdown = get_scenario_markdown(scenario)
        file_writer.write_scenario(scenario, scenario_markdown)
