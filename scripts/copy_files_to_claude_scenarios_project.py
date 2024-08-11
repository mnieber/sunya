from sunya.scripts import sync_files_to_claude

in_landler_fe = "/home/maarten/projects/sunya/src/mock/landler/frontend"
in_landler_be = "/home/maarten/projects/sunya/src/mock/landler/backend"
in_prompts = "/home/maarten/projects/sunya/src/mock/sunya/prompts"

out_landler = "landler/spec"

dir_list = [
    "frontend/modules",
    "frontend/scenarios",
    "backend/modules",
    "backend/scenarios",
]

file_map = {
    f"{in_landler_fe}/modules/checklist.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/modules/frames.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/modules/organizations.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/modules/maps.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/modules/user_settings.py": f"{out_landler}/frontend/modules",
    f"{in_landler_fe}/scenarios/ms2_a_user_signs_in.py": f"{out_landler}/scenarios",
    f"{in_prompts}": "instructions",
}

if __name__ == "__main__":
    args = sync_files_to_claude.parse_args()
    files_copied = sync_files_to_claude.sync_files(file_map, dir_list, args.target_dir)

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
