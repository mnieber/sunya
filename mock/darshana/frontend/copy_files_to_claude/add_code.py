def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/api/types/*T.ts": f"{code}/api/types",
            f"{code_in}/steps/hooks/useStepTreeContext.ts": f"{code}/steps/hooks",
            f"{code_in}/scenarios/hooks/useScenariosContext.ts": f"{code}/scenarios/hooks",
        }
    )
    dir_list += [
        f"{code}/api/types",
        f"{code}/steps/hooks",
        f"{code}/scenarios/hooks",
    ]
