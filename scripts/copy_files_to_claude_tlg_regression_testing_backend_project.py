import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import sync_files_to_local_claude_dir
from mock.tlg_regression_testing.backend.copy_files_to_claude.add_code import add_code
from mock.tlg_regression_testing.backend.copy_files_to_claude.add_instructions import (
    add_instructions,
)
from mock.tlg_regression_testing.backend.copy_files_to_claude.add_sample_code import (
    add_sample_code,
)
from mock.tlg_regression_testing.backend.copy_files_to_claude.add_spec import add_spec

in_mock = "/home/maarten/projects/sunya/src/mock"
in_blogs_be = "/home/maarten/projects/sunya/src/blogs_be"
in_tlg_regression_testing_be = "/home/maarten/projects/landler/src/platform/libs/tlg_regression_testing/src/tlg_regression_testing"


dir_list = [
    "mocks/queries",
]

file_map = {}


add_spec(file_map, dir_list, in_mock=in_mock)
add_instructions(file_map, dir_list, in_mock=in_mock)
add_sample_code(file_map, dir_list, sample_code_in=f"{in_blogs_be}")
add_code(file_map, dir_list, code_in=f"{in_tlg_regression_testing_be}")


if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
