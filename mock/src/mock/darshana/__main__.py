from pathlib import Path
from sunya import FileWriter
from sunya.runtime import wipe_spec_files, parse_args, write_specs

config = dict(
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
    file_writer = FileWriter("darshana/md_specs")
    wipe_spec_files(file_writer)
    root_dirname = Path(__file__).parent
    for package, spec_paths in config["spec_paths_by_package"].items():
        write_specs(root_dirname, package, spec_paths, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
