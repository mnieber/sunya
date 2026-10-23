def filepath_to_import_path(filepath):
    filepath_str = str(filepath)
    if filepath_str.endswith(".py"):
        filepath_str = filepath_str[:-3]

    module_path = filepath_str.replace("/", ".")
    return module_path
