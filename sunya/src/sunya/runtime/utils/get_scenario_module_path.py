def get_scenario_module_path(config, scenario_name):
    scenario_path = config["scenario_path_by_name"].get(scenario_name)
    if scenario_path:
        return scenario_path

    parts = scenario_name.split("/")
    assert len(parts) == 2
    layer, scenario_fn = parts
    return layer, config["scenario_path_tpl"].format(
        layer=layer, scenario_fn=scenario_fn
    )
