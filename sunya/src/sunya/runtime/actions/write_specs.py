import importlib
from pathlib import Path

from sunya.modules.rules.module_namespace_to_tree import module_namespace_to_tree
from sunya.modules.utils.module_namespace import M
from sunya.runtime.actions.get_module_markdown import get_module_markdown
from sunya.runtime.rules.get_scenario_markdown import get_scenario_markdown
from sunya.runtime.utils.file_writer import FileWriter
from sunya.runtime.utils.filepath_to_import_path import filepath_to_import_path
from sunya.runtime.utils.get_module_spec_paths import get_module_spec_paths
from sunya.runtime.utils.get_scenario_spec_paths import get_scenario_spec_paths
from sunya.scenarios.models.scenario import get_scenario
from sunya.scenarios.utils.global_namespace import G  # noqa
from sunya.runtime.rules.get_markdown_signature import get_markdown_signature


def write_specs(
    root_dirname, package, spec_paths, file_writer: FileWriter, package_output_path=None
):
    M.clear()
    G.clear()

    # Default to package name if no custom output path provided
    if package_output_path is None:
        package_output_path = package

    # Write scenarios
    scenario_spec_paths = get_scenario_spec_paths(
        root_dirname, spec_paths["scenario_paths"]
    )
    _write_scenarios(package_output_path, scenario_spec_paths, file_writer)

    # Write modules
    module_spec_paths = get_module_spec_paths(root_dirname, spec_paths["module_paths"])
    _write_modules(package_output_path, module_spec_paths, file_writer)

    watch_paths = set()
    watch_paths.update(Path(root_dirname) / Path(path) for path in scenario_spec_paths)
    watch_paths.update(Path(root_dirname) / Path(path) for path in module_spec_paths)
    return watch_paths


def _write_scenarios(package, scenario_spec_paths, file_writer: FileWriter):
    for scenario_module_path in scenario_spec_paths:
        importlib.import_module(filepath_to_import_path(scenario_module_path))
        scenario = get_scenario()
        scenario_markdown = get_scenario_markdown(scenario)
        scenario.markdown_fn = file_writer.write_scenario(
            package, scenario, get_markdown_signature() + scenario_markdown
        )


def _write_modules(package, module_spec_paths, file_writer):
    dynamic_trees = module_namespace_to_tree(M)
    for module_spec_path in module_spec_paths:
        module_markdown = get_module_markdown(
            module_spec_path,
            dynamic_trees,
        )
        if not module_markdown:
            continue

        # Derive module name from file path
        module_name = Path(module_spec_path).stem

        # Write to file
        file_writer.write_module(
            package, module_name, get_markdown_signature() + module_markdown
        )
