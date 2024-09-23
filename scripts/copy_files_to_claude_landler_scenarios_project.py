import sync_files_to_local_claude_dir

in_landler_spec = "/home/maarten/projects/sunya/src/mock/landler/spec"

in_blogs_prompts = "/home/maarten/projects/sunya/src/mock/blogs/spec/prompts"
in_blogs_be = "/home/maarten/projects/sunya/src/mock/blogs/backend"
in_blogs_fe = "/home/maarten/projects/sunya/src/mock/blogs/frontend"
blogs = "blogs"

landler = "landler"
in_landler_fe = "/home/maarten/projects/sunya/src/mock/landler/frontend"
in_landler_be = "/home/maarten/projects/sunya/src/mock/landler/backend"


dir_list = [
    f"instructions/{blogs}/frontend/modules",
    f"instructions/{blogs}/frontend/scenarios",
    f"instructions/{blogs}/backend/modules",
    f"instructions/{blogs}/backend/scenarios",
    f"spec/roadmaps",
    f"spec/frontend/modules",
    f"spec/frontend/scenarios",
    f"spec/backend/modules",
    f"spec/backend/scenarios",
]

file_map = {
    f"{in_blogs_prompts}/instructions*.md": "instructions",
    f"{in_blogs_fe}/modules/*.py": f"instructions/{blogs}/frontend/modules",
    f"{in_blogs_fe}/scenarios/*.py": f"instructions/{blogs}/frontend/scenarios",
    f"{in_blogs_be}/modules/*.py": f"instructions/{blogs}/backend/modules",
    f"{in_blogs_be}/scenarios/*.py": f"instructions/{blogs}/backend/scenarios",
    f"{in_landler_spec}/roadmaps/*.md": f"spec/roadmaps",
    f"{in_landler_fe}/modules/*.py": f"spec/frontend/modules",
    f"{in_landler_fe}/scenarios/*.py": f"spec/frontend/scenarios",
    f"{in_landler_be}/modules/*.py": f"spec/backend/modules",
    f"{in_landler_be}/scenarios/*.py": f"spec/backend/scenarios",
}

if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
