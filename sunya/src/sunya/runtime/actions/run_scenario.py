import importlib

from sunya.scenarios.models.scenario_context import get_scenario_context


def run_scenario(scenario_pkg):
    from sunya import get_scenario

    if isinstance(scenario_pkg, str):
        scenario_module = importlib.import_module(f"{scenario_pkg}.scenario")
        steps_module_path = f"{scenario_pkg}.impl.steps"
    else:
        scenario_module = scenario_pkg
        steps_module_path = f"{scenario_module.__package__}.impl.steps"

    scenario_name = getattr(scenario_module, "scenario_name")
    assert scenario_name, f"scenario_name not found in {scenario_module}"

    if scenario := get_scenario(scenario_name):
        return scenario

    try:
        steps_module = importlib.import_module(steps_module_path)
    except ImportError as e:
        steps_module = None

    if steps_module:
        implement_step_memo = get_scenario_context().implement_step
        get_scenario_context().implement_step = getattr(steps_module, "implement_step")

    run_fn = getattr(scenario_module, "run")
    scenario = run_fn()

    if steps_module:
        get_scenario_context().implement_step = implement_step_memo

    return scenario
