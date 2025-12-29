import os
from pathlib import Path
from sunya import FileWriter
from sunya.runtime import (
    wipe_spec_files,
    write_specs,
    parse_args,
)


config = dict(
    output_dir="md_specs",
    spec_paths_by_package=dict(
        backend=dict(
            scenario_paths=["backend/scenarios/**/scenario.py"],
            module_paths=["backend/modules/*.py"],
        ),
        frontend=dict(
            scenario_paths=["frontend/scenarios/**/scenario.py"],
            module_paths=["frontend/modules/*.py"],
        ),
    ),
)


def run(args):
    root_dirname = Path(__file__).parent
    file_writer = FileWriter(os.path.join(root_dirname, config["output_dir"]))
    for package, spec_paths in config["spec_paths_by_package"].items():
        wipe_spec_files(file_writer, package)
        write_specs(root_dirname, package, spec_paths, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
