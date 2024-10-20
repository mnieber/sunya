def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/examples/actions/*.py": f"{code}/examples/actions",
            f"{code_in}/examples/models/*.py": f"{code}/examples/models",
            f"{code_in}/examples/rules/*.py": f"{code}/examples/rules",
            f"{code_in}/rtest.py": f"{code}",
            f"{code_in}/run/actions/*.py": f"{code}/run/actions",
            f"{code_in}/run/models/*.py": f"{code}/run/models",
            f"{code_in}/run/rules/*.py": f"{code}/run/rules",
            f"{code_in}/run/utils/*.py": f"{code}/run/utils",
            f"{code_in}/selectors/actions/*.py": f"{code}/selectors/actions",
            f"{code_in}/selectors/models/*.py": f"{code}/selectors/models",
            f"{code_in}/settings.py": f"{code}",
            f"{code_in}/storage/*.py": f"{code}/storage",
            f"{code_in}/test_report/actions/*.py": f"{code}/test_report/actions",
            f"{code_in}/test_report/models/*.py": f"{code}/test_report/models",
        }
    )
    dir_list += [
        f"{code}/examples/actions",
        f"{code}/examples/models",
        f"{code}/examples/rules",
        f"{code}/run/actions",
        f"{code}/run/models",
        f"{code}/run/rules",
        f"{code}/run/utils",
        f"{code}/selectors/actions",
        f"{code}/selectors/models",
        f"{code}/storage",
        f"{code}/test_report/actions",
        f"{code}/test_report/models",
    ]
