import importlib


def run_scenario(scenario):
    from sunya import get_scenario

    if isinstance(scenario, str):
        scenario_pkg = importlib.import_module(scenario)
    else:
        scenario_pkg = scenario

    scenario_name = getattr(scenario_pkg, "scenario_name")
    assert scenario_name, f"scenario_name not found in {scenario_pkg}"

    if scenario := get_scenario(scenario_name):
        return scenario

    run_fn = getattr(scenario_pkg, "run")
    scenario = run_fn()
    return scenario
