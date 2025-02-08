def add_instructions(file_map, dir_list, in_mock):
    instructions = "instructions"
    in_blogs_be_spec = f"{in_mock}/blogs/spec"

    in_be_code_instructions = f"{in_mock}/blogs/backend/spec/prompts"
    file_map.update(
        {
            f"{in_be_code_instructions}/instructions*.md": f"{instructions}",
            f"{in_blogs_be_spec}/backend/modules": f"{instructions}/spec/backend/modules",
            f"{in_blogs_be_spec}/backend/scenarios": f"{instructions}/spec/backend/scenarios",
        }
    )
    dir_list += [
        f"{instructions}",
        f"{instructions}/spec/backend/modules",
        f"{instructions}/spec/backend/scenarios",
    ]
