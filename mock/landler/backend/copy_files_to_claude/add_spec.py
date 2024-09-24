def add_spec(file_map, dir_list, in_mock):
    in_landler_spec = f"{in_mock}/landler/spec"

    file_map.update(
        {
            f"{in_landler_spec}/roadmaps/*.md": "spec/roadmaps",
            f"{in_landler_spec}/backend/modules": "spec/backend/modules",
            f"{in_landler_spec}/backend/scenarios": "spec/backend/scenarios",
        }
    )
    dir_list += [
        "spec/roadmaps",
        "spec/backend/modules",
        "spec/backend/scenarios",
    ]
