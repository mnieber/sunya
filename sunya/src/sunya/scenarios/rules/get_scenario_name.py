import os


def get_scenario_name(file_path):
    return os.path.basename(file_path).replace(".py", "")
