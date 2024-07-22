import importlib


def run_scenario(scenario_path):
    scenario_pkg = importlib.import_module(scenario_path)
    run_fn = getattr(scenario_pkg, "run")
    scenario = run_fn()
    return scenario
