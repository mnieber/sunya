def get_scenario_names(config, args):
    use_all_scenarios = args.all or args.scenario == "all"
    scenario_names = (
        config["all_scenario_names"]
        if use_all_scenarios
        else [args.scenario] if args.scenario else []
    )

    return scenario_names
