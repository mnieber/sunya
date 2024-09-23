from argparse import ArgumentParser
import os
from dodo_commands import Dodo


def _args():
    # Create the parser
    parser = ArgumentParser(description="")
    parser.add_argument(
        "project",
        choices=[
            "landler_scenarios",
            "landler_backend",
            "landler_frontend",
            "darshana_scenarios",
            "darshana_frontend",
            "darshana_backend",
        ],
    )
    parser.add_argument("--skip-upload", action="store_true")

    # Use the parser to create the command arguments
    args = Dodo.parse_args(parser, config_args=[])
    args.cwd = Dodo.get("/ROOT/project_dir")

    return args


# Use safe=False if the script makes changes other than through Dodo.run
if Dodo.is_main(__name__, safe=True):
    args = _args()
    config_file = f"/home/maarten/.claudesync/{args.project}.json"
    if not os.path.exists(config_file):
        raise Exception(f"Config file {config_file} does not exist")

    sunya_dir = f"/home/maarten/projects/sunya"
    local_dir = f"{sunya_dir}/res/claude/{args.project}"
    if not os.path.exists(local_dir):
        raise Exception(f"Local dir {local_dir} does not exist")

    copy_script = (
        f"{sunya_dir}/src/scripts/copy_files_to_claude_{args.project}_project.py"
    )
    if not os.path.exists(copy_script):
        raise Exception(f"Script {copy_script} does not exist")

    Dodo.run(
        [
            "python",
            copy_script,
            local_dir,
            "-v",
        ]
    )

    if not args.skip_upload:
        Dodo.run(
            [
                "cp",
                config_file,
                f"/home/maarten/.claudesync/config.json",
            ]
        )

        Dodo.run(
            [
                "claudesync",
                "project",
                "sync",
            ]
        )
