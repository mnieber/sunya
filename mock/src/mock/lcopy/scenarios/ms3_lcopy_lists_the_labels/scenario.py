from sunya import (
    the,
    goal,
    add_scenario,
    get_scenario,
    G as g,
    R as r,
    I as i,
    it,
    comment,
)

scenario_name = f"backend/ms1_lcopy_lists_the_labels"


def start():
    with add_scenario(scenario_name):
        with goal(i.list_the(r.labels).in_the(r.config_files)):
            with (
                the(g.user)
                .calls_the(g.lcopy_tool)
                .with_the(r.options_file)
                .and_the_listlabels_command()
            ):
                comment("lcopy --options <options_file> listlabels")

                with it().calls_the(g.parse_options_file_action):
                    assert r.options

                with (
                    it()
                    .calls_the(g.resolve_includes_rule)
                    .on_each(r.config_file)
                    .in_the(r.options_file)
                    .to_obtain_a(r.list_of_config_files)
                ):
                    assert r.list_of_config_files

                with (
                    it()
                    .outputs_all(r.labels)
                    .that_are_present_in_the_target_directories_of_the(
                        r.list_of_config_files
                    )
                ):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
