import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import sync_files_to_local_claude_dir
from mock.darshana.frontend.copy_files_to_claude.add_spec import add_spec
from mock.darshana.frontend.copy_files_to_claude.add_sample_code import add_sample_code
from mock.darshana.frontend.copy_files_to_claude.add_instructions import (
    add_instructions,
)

in_mock = "/home/maarten/projects/sunya/src/mock"
in_landler_fe = "/home/maarten/projects/sunya/src/landler_fe"


dir_list = [
    "mocks/queries",
    "routes",
    "stories",
]

file_map = {}


add_spec(file_map, dir_list, in_mock=in_mock)
add_instructions(file_map, dir_list, in_mock=in_mock)
add_sample_code(file_map, dir_list, sample_code_in=f"{in_landler_fe}/src")


if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
