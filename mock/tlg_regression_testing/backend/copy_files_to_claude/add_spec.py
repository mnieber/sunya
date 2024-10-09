def add_spec(file_map, dir_list, in_mock):
    in_tlg_regression_testing_spec = f"{in_mock}/tlg_regression_testing/spec"

    file_map.update(
        {
            f"{in_tlg_regression_testing_spec}/roadmap.md": "spec",
            f"{in_tlg_regression_testing_spec}/backend/modules": "spec/backend/modules",
            f"{in_tlg_regression_testing_spec}/backend/scenarios": "spec/backend/scenarios",
        }
    )
    dir_list += [
        "spec",
        "spec/backend/modules",
        "spec/backend/scenarios",
    ]
