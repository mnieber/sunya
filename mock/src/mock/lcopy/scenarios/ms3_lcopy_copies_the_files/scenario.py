from sunya import G as g
from sunya import I as i
from sunya import R as r
from sunya import add_scenario, get_scenario, goal, it, the

scenario_name = f"backend/ms3_lcopy_copies_the_files"


def start():
    with add_scenario(scenario_name):
        with goal(i.copy_the(r.files).in_the(r.target_nodes)):
            with (
                the(g.lcopy_tool)
                .calls_the(g.copy_files_action)
                .with_the(r.target_nodes)
                .and_options_from_the(r.config)
            ):
                with it().works_with_concrete_file_paths_in_target_nodes():
                    """
                    The copy_files_action receives target_nodes with filename_patterns that contain
                    only concrete file paths (not glob patterns or exclusion rules). This is because
                    the parse_target_node_action has already processed all patterns and produced a
                    list of specific files to be copied.
                    """
                    assert (
                        r.target_node.filename_patterns
                    )  # Contains concrete file paths, not patterns

                with it().copies_each_specified_file_to_the_destination():
                    """
                    For each concrete file path in target_node.filename_patterns, the copy_files_action
                    copies the file to the appropriate destination path, maintaining the appropriate
                    directory structure.

                    The destination directory structure mirrors the structure defined by the target nodes,
                    not the original source directory structure.
                    """

                with it().respects_the_overwrite_option():
                    """
                    The copy_files_action respects the 'overwrite' option (which can be 'skip',
                    'overwrite', or 'prompt') when deciding whether to overwrite existing files
                    in the destination directory.
                    """

                with it().respects_the_dry_run_flag():
                    """
                    When the dry_run flag is set in the options, the copy_files_action should not
                    actually modify any files or directories, but should output what actions would
                    be taken as if the copy was being performed.
                    """

                with it().tracks_all_copied_files():
                    """
                    The copy_files_action keeps track of all files that were copied (or would be copied
                    in the case of a dry run) and returns this list. This list can later be used by
                    other actions, such as the purge_files_action.
                    """
                    assert r.list_of_copied_files

        with goal(i.purge_unwanted_files_from_the_(r.destination).directory()):
            with (
                the(g.lcopy_tool)
                .calls_the(g.purge_files_action)
                .with_the(r.destination)
                .and_the(r.list_of_copied_files)
            ):
                with it().removes_files_not_in_the(r.list_of_copied_files):
                    """
                    The purge_files_action removes any files in the destination directory
                    that are not in the list of copied files. This ensures that the destination
                    directory contains only the files that were explicitly copied by the
                    copy_files_action.
                    """

                with it().also_respects_the_dry_run_flag():
                    """
                    Just like the copy_files_action, the purge_files_action respects the
                    dry_run flag and only outputs what actions would be taken without
                    actually removing any files when dry_run is True.
                    """

        with goal(i.optionally_create_a_concatenated_output_file()):
            with (
                the(g.lcopy_tool)
                .calls_the(g.create_concatenated_output_action)
                .with_the(r.source_dirname)
                .and_the(r.output_filename)
            ):
                with it().combines_all_files_into_a_single_output_file():
                    """
                    The create_concatenated_output_action combines all the files in the
                    source directory (which is the destination of the copy operation)
                    into a single output file, with appropriate separators between files.
                    """

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
