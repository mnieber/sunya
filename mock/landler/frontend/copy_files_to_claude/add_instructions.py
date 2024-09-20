def add_instructions(file_map, dir_list, in_mock):
    instructions = "instructions"
    in_blogs_fe_spec = f"{in_mock}/blogs/spec"

    in_fe_code_instructions = f"{in_mock}/blogs/frontend/spec/prompts"
    file_map.update(
        {
            f"{in_fe_code_instructions}/instructions*.md": f"{instructions}",
            f"{in_blogs_fe_spec}/frontend/modules": f"{instructions}/spec/frontend/modules",
            f"{in_blogs_fe_spec}/frontend/scenarios": f"{instructions}/spec/frontend/scenarios",
        }
    )
    dir_list += [
        f"{instructions}",
        f"{instructions}/spec/frontend/modules",
        f"{instructions}/spec/frontend/scenarios",
    ]
