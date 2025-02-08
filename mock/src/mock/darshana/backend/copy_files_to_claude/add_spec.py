def add_spec(file_map, dir_list, in_mock):
    in_darshana_spec = f"{in_mock}/darshana/spec"

    file_map.update(
        {
            f"{in_darshana_spec}/roadmap.md": "spec",
            f"{in_darshana_spec}/backend/modules": "spec/backend/modules",
            f"{in_darshana_spec}/backend/scenarios": "spec/backend/scenarios",
        }
    )
    dir_list += [
        "spec",
        "spec/backend/modules",
        "spec/backend/scenarios",
    ]
