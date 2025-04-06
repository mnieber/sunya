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
            with the(g.user).calls_the(g.lcopy_tool).with_the_listlabels_command():
                comment("lcopy --options <options_file> listlabels")

                with it().calls_the(g.parse_options_file_action):
                    assert r.options

                with (
                    it()
                    .calls_the(g.get_list_of_labels_rule)
                    .to_parse_the(r.config_file)
                    .and_output_all(r.labels)
                    .that_are_present_in_the_target_nodes()
                ):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
