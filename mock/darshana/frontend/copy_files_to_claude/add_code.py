def add_code(file_map, dir_list, sample_code_in):
    sample_code = "src"
    file_map.update(
        {
            f"{sample_code_in}/api/types/*T.ts": f"{sample_code}/api/types",
        }
    )
    dir_list += [
        f"{sample_code}/api/types",
    ]
