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
                with it().uses_the(r.target_node.filename_patterns).to_determine_the(
                    r.list_of_excluded_patterns
                ):
                    assert r.list_of_excluded_patterns

                with it().uses_the(r.target_node.filename_patterns).to_determine_the(
                    r.list_of_filenames
                ):
                    """
                    Every filename pattern that is not an exclude pattern is combined with the source_dirname
                    to create a glob pattern. The glob pattern is used to find the list of filenames.
                    """
                    assert r.list_of_filenames

                with (
                    it()
                    .uses_the(g.get_filtered_files_rule)
                    .to_filter_out_the_excluded_and_ignored_files()
                ):
                    # The r.list_of_filenames will now be smaller
                    assert r.list_of_filenames

                with it().copies(g.list_of_filenames).to_the(r.destination).directory():
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
