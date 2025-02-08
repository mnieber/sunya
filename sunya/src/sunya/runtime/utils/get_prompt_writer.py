import importlib


def get_prompt_writer(config, layer):
    prompt_writer_path = config["prompt_writer_path_tpl"].format(layer=layer)
    prompt_writer_pkg = importlib.import_module(prompt_writer_path)
    prompt_writer_class = getattr(prompt_writer_pkg, "PromptWriter")
    return prompt_writer_class()
