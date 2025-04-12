from sunya import the, goal, add_scenario, get_scenario, G as g, R as r, I as i, it

scenario_name = f"backend/ms3_lcopy_copies_the_files"


def start():
    with add_scenario(scenario_name):
        with goal(i.copy_the(r.files).in_the(r.target_nodes)):
            with (
                the(g.lcopy_tool)
                .calls_the(g.copy_files_action)
                .with_the(r.target_nodes)
                .and_the(r.options)
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
                    """
                    pass

                with it().respects_the_dry_run_flag():
                    """
                    When the dry_run flag is set in the options, the copy_files_action should not
                    actually modify any files or directories, but should output what actions would
                    be taken as if the copy was being performed.
                    """
                    pass

                with it().tracks_all_copied_files():
                    """
                    The copy_files_action keeps track of all files that were copied (or would be copied
                    in the case of a dry run) and returns this list. This list can later be used by
                    other actions, such as the purge_files_action, which is called separately from
                    the main entry point rather than within the copy_files_action.
                    """
                    assert r.list_of_copied_files

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
