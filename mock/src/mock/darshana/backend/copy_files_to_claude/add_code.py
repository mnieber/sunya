def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/actors/actions/*.py": f"{code}/actors/actions",
            f"{code_in}/actors/models.py": f"{code}/actors",
            f"{code_in}/actors/tests/factories.py": f"{code}/actors/tests",
            f"{code_in}/projects/models.py": f"{code}/projects",
            f"{code_in}/projects/actions/*.py": f"{code}/projects/actions",
            f"{code_in}/projects/tests/factories.py": f"{code}/projects/tests",
            f"{code_in}/scenarios/actions/*.py": f"{code}/scenarios/actions",
            f"{code_in}/scenarios/models.py": f"{code}/scenarios",
            f"{code_in}/scenarios/tests/factories.py": f"{code}/scenarios/tests",
            f"{code_in}/steps/actions/*.py": f"{code}/steps/actions",
            f"{code_in}/steps/models.py": f"{code}/steps",
            f"{code_in}/steps/tests/factories.py": f"{code}/steps/tests",
        }
    )
    dir_list += [
        f"{code}/actors/actions",
        f"{code}/actors/tests",
        f"{code}/projects/actions",
        f"{code}/projects/tests",
        f"{code}/scenarios/actions",
        f"{code}/scenarios/tests",
        f"{code}/steps/actions",
        f"{code}/steps/tests",
    ]
