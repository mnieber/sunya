def add_code(file_map, dir_list, code_in):
    code = "src"
    file_map.update(
        {
            f"{code_in}/api/types/*T.ts": f"{code}/api/types",
            f"{code_in}/projects/hooks/useProjectLeadsContext.ts": f"{code}/projects/hooks",
            f"{code_in}/projects/hooks/useProjectContext.ts": f"{code}/projects/hooks",
            f"{code_in}/projects/routes.ts": f"{code}/projects",
            f"{code_in}/scenarios/routes.ts": f"{code}/scenarios",
            f"{code_in}/steps/hooks/useStepTreeContext.ts": f"{code}/steps/hooks",
        }
    )
    dir_list += [
        f"{code}/api/types",
        f"{code}/steps/hooks",
        f"{code}/projects",
        f"{code}/projects/hooks",
        f"{code}/scenarios",
    ]
