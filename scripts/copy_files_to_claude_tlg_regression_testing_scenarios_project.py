import sync_files_to_local_claude_dir

in_tlg_regression_testing_spec = (
    "/home/maarten/projects/sunya/src/mock/tlg_regression_testing/spec"
)

tlg_regression_testing = "tlg_regression_testing"
in_tlg_regression_testing_be = (
    "/home/maarten/projects/sunya/src/mock/tlg_regression_testing/backend"
)


dir_list = [
    "tlg_regression_testing/spec",
    "instructions",
    "spec",
    f"{tlg_regression_testing}/backend/modules",
    f"{tlg_regression_testing}/backend/scenarios",
]

file_map = {
    f"{in_tlg_regression_testing_be}/modules/*.py": f"{tlg_regression_testing}/backend/modules",
    f"{in_tlg_regression_testing_be}/scenarios/*.py": f"{tlg_regression_testing}/backend/scenarios",
    f"{in_tlg_regression_testing_spec}/roadmap.md": f"spec",
}

if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
