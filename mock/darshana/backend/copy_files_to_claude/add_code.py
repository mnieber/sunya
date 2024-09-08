def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/actors/models.py": f"{code}/blogs",
            f"{code_in}/actors/actions/*.py": f"{code}/blogs",
        }
    )
    dir_list += [
        f"{code}/blogs",
    ]
