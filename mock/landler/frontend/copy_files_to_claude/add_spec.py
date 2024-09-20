def add_spec(file_map, dir_list, in_mock):
    in_landler_spec = f"{in_mock}/landler/spec"

    file_map.update(
        {
            f"{in_landler_spec}/roadmap.md": "spec",
            f"{in_landler_spec}/frontend/modules": "spec/frontend/modules",
            f"{in_landler_spec}/frontend/scenarios": "spec/frontend/scenarios",
        }
    )
    dir_list += [
        "spec",
        "spec/frontend/modules",
        "spec/frontend/scenarios",
    ]
