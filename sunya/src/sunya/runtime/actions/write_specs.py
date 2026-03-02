import importlib
import sys
from pathlib import Path

from sunya.runtime.rules.get_markdown_signature import get_markdown_signature
from sunya.runtime.utils.file_writer import FileWriter
from sunya.runtime.utils.filepath_to_import_path import filepath_to_import_path
from sunya.runtime.utils.get_scenario_spec_paths import get_scenario_spec_paths
from sunya.scenarios.models.scenario import get_scenario
from sunya.scenarios.utils.component_namespace import C, ComponentSpec


def write_specs(
    root_dirname,
    package,
    spec_config,
    file_writer: FileWriter,
    package_output_path=None,
):
    # Default to package name if no custom output path provided
    if package_output_path is None:
        package_output_path = package

    # Write scenarios
    scenario_spec_paths = get_scenario_spec_paths(
        root_dirname, spec_config["scenario_paths"]
    )
    _write_scenarios(package_output_path, scenario_spec_paths, file_writer)

    # Write modules
    _write_modules(package_output_path, file_writer)

    watch_paths = set()
    watch_paths.update(Path(root_dirname) / Path(path) for path in scenario_spec_paths)
    return watch_paths


def _write_scenarios(package, scenario_spec_paths, file_writer: FileWriter):
    for scenario_module_path in scenario_spec_paths:
        module_name = filepath_to_import_path(scenario_module_path)
        importlib.import_module(module_name)
        scenario = get_scenario()
        scenario_markdown = _get_scenario_markdown(scenario)
        scenario.markdown_fn = file_writer.write_scenario(
            package, scenario, get_markdown_signature() + scenario_markdown
        )
        # Remove module from sys.modules to allow re-import on next run
        if module_name in sys.modules:
            del sys.modules[module_name]


def _write_modules(package, file_writer):
    # TODO: write C as module specs
    print(C)


def _get_component_markdown(component_spec: ComponentSpec):
    markdown_parts = []

    return "".join(markdown_parts)


def _get_scenario_markdown(scenario):
    markdown = f"# Scenario: {scenario.name}\n\n"

    for node in scenario.nodes:
        markdown += f"## {node.title}\n\n{node.markdown.strip()}\n\n"

    return markdown
