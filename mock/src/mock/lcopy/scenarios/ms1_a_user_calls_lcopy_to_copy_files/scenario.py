from sunya import G as g
from sunya import I as i
from sunya import R as r
from sunya import add_scenario, comment, get_scenario, goal, it, the

from .get_example_config import get_example_config
from .get_example_config_file import get_example_config_file

scenario_name = f"backend/ms1_a_user_calls_lcopy_to_copy_files"


def start():
    with add_scenario(scenario_name):
        with goal(i.copy_selected_files_to_the_(r.destination).directory()):
            with the(g.user).calls_the(g.lcopy_tool).with_the_copy_command():
                comment(
                    "lcopy path/to/.lcopy.yaml copy --dry-run --labels organize-dinner-party music-friends"
                )
                comment(get_example_config_file())

                with it().calls_the(g.parse_config_file_action):
                    comment(get_example_config())
                    assert r.config
                    assert r.config.options

                    with (
                        it()
                        .calls_the(g.parse_target_section_action)
                        .to_recursively_parse_target_nodes_in_the(r.config)
                    ):
                        assert r.config.target_nodes

                with (
                    it()
                    .calls_the(g.copy_files_action)
                    .with_the(r.config.target_nodes)
                    .and_receives_back_the(r.list_of_copied_files)
                ):
                    pass

                with (
                    it()
                    .calls_the(g.purge_files_action)
                    .with_the(r.config.options.destination)
                    .directory_and_the(r.list_of_copied_files)
                ):
                    pass

                with (
                    it()
                    .may_call_the(g.create_concatenated_output_action)
                    .if_a_concatenated_output_filename_is_specified()
                ):
                    """
                    If the options specify a concatenated_output_filename, then
                    the create_concatenated_output_action is called to combine
                    all copied files into a single output file.
                    """

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
