def get_module_and_scenario_names(args, all_module_names, all_scenario_names):
    use_all_modules = args.all or args.module == "all"
    module_names = (
        all_module_names if use_all_modules else [args.module] if args.module else []
    )

    use_all_scenarios = args.all or args.scenario == "all"
    scenario_names = (
        all_scenario_names
        if use_all_scenarios
        else [args.scenario] if args.scenario else []
    )

    return module_names, scenario_names
