from sunya import G as g
from sunya import I as i
from sunya import R as r
from sunya import add_scenario, comment, get_scenario, goal, it, the

scenario_name = f"backend/ms4_lcopy_lists_the_labels"


def start():
    with add_scenario(scenario_name):
        with goal(i.list_the(r.labels).in_the(r.config_files)):
            with the(g.user).calls_the(g.lcopy_tool).with_the_listlabels_command():
                comment("lcopy path/to/.lcopy.yaml listlabels")

                with it().calls_the(g.parse_config_file_action):
                    assert r.config

                with (
                    it()
                    .calls_the(g.get_list_of_labels_rule)
                    .to_parse_the(r.config_file)
                    .and_output_all(r.labels)
                    .that_are_present_in_the_target_nodes()
                ):
                    """
                    The get_list_of_labels_rule extracts all labels from the config file
                    by examining the targets section. It also recursively examines any
                    source configs that are referenced to collect their labels as well.
                    """
                    assert r.list_of_labels

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
