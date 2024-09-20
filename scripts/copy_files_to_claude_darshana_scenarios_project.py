import sync_files_to_local_claude_dir

in_darshana_spec = "/home/maarten/projects/sunya/src/mock/darshana/spec"

in_blogs_prompts = "/home/maarten/projects/sunya/src/mock/blogs/spec/prompts"
in_blogs_be = "/home/maarten/projects/sunya/src/mock/blogs/backend"
in_blogs_fe = "/home/maarten/projects/sunya/src/mock/blogs/frontend"
blogs = "blogs"

darshana = "darshana"
in_darshana_fe = "/home/maarten/projects/sunya/src/mock/darshana/frontend"
in_darshana_be = "/home/maarten/projects/sunya/src/mock/darshana/backend"


dir_list = [
    "darshana/spec",
    "instructions",
    "spec",
    f"{blogs}/frontend/modules",
    f"{blogs}/frontend/scenarios",
    f"{blogs}/backend/modules",
    f"{blogs}/backend/scenarios",
    f"{darshana}/frontend/modules",
    f"{darshana}/frontend/scenarios",
    f"{darshana}/backend/modules",
    f"{darshana}/backend/scenarios",
]

file_map = {
    f"{in_blogs_be}/modules/*.py": f"{blogs}/backend/modules",
    f"{in_blogs_be}/scenarios/*.py": f"{blogs}/backend/scenarios",
    f"{in_blogs_fe}/modules/*.py": f"{blogs}/frontend/modules",
    f"{in_blogs_fe}/scenarios/*.py": f"{blogs}/frontend/scenarios",
    f"{in_blogs_prompts}/instructions*.md": "instructions",
    f"{in_darshana_be}/modules/*.py": f"{darshana}/backend/modules",
    f"{in_darshana_be}/scenarios/*.py": f"{darshana}/backend/scenarios",
    f"{in_darshana_fe}/modules/*.py": f"{darshana}/frontend/modules",
    f"{in_darshana_fe}/scenarios/*.py": f"{darshana}/frontend/scenarios",
    f"{in_darshana_spec}/roadmap.md": f"spec",
}

if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
