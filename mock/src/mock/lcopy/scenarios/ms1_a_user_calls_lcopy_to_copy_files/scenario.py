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

from .get_example_options_file import get_example_options_file
from .get_example_config_file import get_example_config_file
from .get_example_config import get_example_config

scenario_name = f"backend/ms1_a_user_calls_lcopy_to_copy_files"


def start():
    with add_scenario(scenario_name):
        with goal(i.copy_selected_files_to_the_(r.destination).directory()):
            with the(g.user).calls_the(g.lcopy_tool).with_the_copy_command():
                comment("lcopy --options <options_file> copy --dry-run")
                comment(get_example_options_file())

                with it().calls_the(g.parse_options_file_action):
                    assert r.options

                with (
                    it()
                    .calls_the(g.parse_config_file_action)
                    .to_parse_each(r.config_file)
                    .in_the(r.options.config_fns)
                ):
                    comment(get_example_config_file())
                    comment(get_example_config())

                    with (
                        it()
                        .calls_the(g.parse_target_node_action)
                        .to_recursively_parse_each(r.target_node)
                        .in_the(r.config)
                        .and_add_them_to_the(r.config.target_nodes)
                    ):
                        assert r.config.target_nodes

                    assert r.list_of_configs

                with (
                    it()
                    .calls_the(g.copy_files_action)
                    .with_the(r.target_nodes)
                    .and_receives_back_the(r.list_of_copied_files)
                ):
                    pass

                with (
                    it()
                    .calls_the(g.purge_files_action)
                    .with_the(r.destination)
                    .directory_and_the(r.list_of_copied_files)
                ):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
