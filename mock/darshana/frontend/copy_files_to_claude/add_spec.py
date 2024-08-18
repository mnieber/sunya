def add_spec(file_map, dir_list, in_mock):
    in_darshana_fe_spec = f"{in_mock}/darshana/spec"

    file_map.update(
        {
            f"{in_darshana_fe_spec}/roadmap.md": "spec",
            f"{in_darshana_fe_spec}/frontend/modules": "spec/frontend/modules",
            f"{in_darshana_fe_spec}/frontend/scenarios": "spec/frontend/scenarios",
        }
    )
    dir_list += [
        "spec",
        "spec/frontend/modules",
        "spec/frontend/scenarios",
    ]
