def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/api/types/*T.ts": f"{code}/api/types",
        }
    )
    dir_list += [
        f"{code}/api/types",
    ]
