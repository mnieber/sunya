import sync_files_to_local_claude_dir

in_landler_spec = "/home/maarten/projects/sunya/src/mock/landler/spec"
in_landler_fe = "/home/maarten/projects/sunya/src/mock/landler/frontend"
in_landler_be = "/home/maarten/projects/sunya/src/mock/landler/backend"
out_landler = "landler"

in_blogs_spec = "/home/maarten/projects/sunya/src/mock/blogs/spec"
in_blogs_fe = "/home/maarten/projects/sunya/src/mock/blogs/frontend"
in_blogs_be = "/home/maarten/projects/sunya/src/mock/blogs/backend"
out_blogs = "blogs"

in_prompts = "/home/maarten/projects/sunya/src/mock/sunya/prompts"


dir_list = [
    "blogs/spec",
    "instructions",
    "blogs/frontend/modules",
    "blogs/frontend/scenarios",
    "blogs/backend/modules",
    "blogs/backend/scenarios",
    "landler/spec",
    "landler/frontend/modules",
    "landler/frontend/scenarios",
    "landler/backend/modules",
    "landler/backend/scenarios",
]

file_map = {
    f"{in_blogs_spec}/roadmap.md": f"{out_blogs}/spec",
    f"{in_blogs_fe}/modules/*.py": f"{out_blogs}/frontend/modules",
    f"{in_blogs_fe}/scenarios/*.py": f"{out_blogs}/frontend/scenarios",
    f"{in_blogs_be}/modules/*.py": f"{out_blogs}/backend/modules",
    f"{in_blogs_be}/scenarios/*.py": f"{out_blogs}/backend/scenarios",
    f"{in_landler_spec}/roadmap.md": f"{out_landler}/spec",
    f"{in_landler_fe}/modules/*.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/scenarios/*.py": f"{out_landler}/frontend/scenarios",
    f"{in_landler_be}/modules/*.py": f"{out_landler}/backend/modules",
    f"{in_landler_be}/scenarios/*.py": f"{out_landler}/backend/scenarios",
    f"{in_prompts}/instructions*.md": "instructions",
}

if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
