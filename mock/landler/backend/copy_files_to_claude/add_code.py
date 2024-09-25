def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/organizations/actions/*.py": f"{code}/organizations/actions",
            f"{code_in}/organizations/models.py": f"{code}/organizations",
            f"{code_in}/organizations/tests/factories.py": f"{code}/organizations/tests",
            f"{code_in}/checklists/actions/*.py": f"{code}/checklists/actions",
            f"{code_in}/checklists/models.py": f"{code}/checklists",
        }
    )
    dir_list += [
        f"{code}/organizations/actions",
        f"{code}/organizations/tests",
        f"{code}/checklists/actions",
        f"{code}/checklists/tests",
    ]
