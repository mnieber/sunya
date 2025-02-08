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

scenario_name = f"backend/ms1_lcopy_copies_the_files"


def start():
    with add_scenario(scenario_name):
        with goal(i.copy_the(r.file_set).to_the(r.target_directory)):
            with (
                the(g.user)
                .calls_the(g.lcopy_tool)
                .with_the(r.options_file)
                .and_the_copy_command()
            ):
                comment("lcopy --options <options_file> copy")
                comment(get_example_options_file())

                with it().calls_the(g.parse_options_file_action):
                    comment(it().expands_env_vars_and_the_home_dir_in_all_filepaths())
                    assert r.options

                with (
                    it()
                    .calls_the(g.parse_config_file_action)
                    .for_each(r.config_file)
                    .in_the(r.options)
                ):
                    comment(get_example_config_file())
                    assert r.list_of_root_config_nodes

                with it().creates_an_empty(r.file_map_tree):
                    pass

                with (
                    it()
                    .calls_the(g.process_config_action)
                    .for_each(r.root_config_node)
                    .in_the(r.list_of_root_config_nodes)
                ):
                    assert r.file_map_tree

                with (
                    it()
                    .calls_the(g.copy_files_action)
                    .with_the(r.file_map_tree)
                    .and_received_back_the(r.list_of_copied_files)
                ):
                    pass

                with it().calls_the(g.purge_files_action).with_the(
                    r.list_of_copied_files
                ):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
