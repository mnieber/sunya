import sync_files_to_local_claude_dir

in_darshana_spec = "/home/maarten/projects/darshana/src/mock/darshana/spec"

in_prompts = "/home/maarten/projects/sunya/src/mock/darshana/prompts"


dir_list = [
    "darshana/spec",
    "instructions",
]

file_map = {
    f"{in_darshana_spec}/roadmap.md": f"spec",
    f"{in_prompts}/instructions*.md": "instructions",
}

if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
