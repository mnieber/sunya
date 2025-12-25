def get_scenario_module_paths(config, args):
    use_all_scenarios = args.all or args.scenario == "all"
    scenario_module_paths = (
        config["all_scenario_paths"]
        if use_all_scenarios
        else [args.scenario] if args.scenario else []
    )

    return scenario_module_paths
