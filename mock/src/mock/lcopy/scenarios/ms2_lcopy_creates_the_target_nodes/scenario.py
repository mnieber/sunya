from sunya import G as g
from sunya import R as r
from sunya import add_scenario, comment, get_scenario, it, the

scenario_name = f"backend/ms2_lcopy_creates_the_target_nodes"


def start():
    with add_scenario(scenario_name):
        with (
            the(g.parse_config_file_action)
            .calls_the(g.parse_target_section_action)
            .with_a(r.config)
            .to_populate_the(r.config.target_nodes)
        ):
            comment(
                """
            The parse_target_section_action examines the targets section of a config file,
            processes each label that matches the requested labels, and adds the
            resulting target nodes to the config.target_nodes list.

            It also processes any includes by loading the appropriate source config files
            and extracting their target nodes.
            """
            )

            with it().processes_includes_in_the_config_file():
                """
                For each include reference like "source_alias.label" in the includes section,
                the parse_target_section_action loads the source config file and extracts the
                target nodes for the specified label.

                The loaded target nodes are added to the current config's target_nodes list.

                A skiplist is used to process the same combination of source alias and label twice.
                """

            with (
                it()
                .calls_the(g.parse_target_node_action)
                .for_each_target_in_the_config_file()
            ):
                with it().may_determine_that_the(
                    r.target_basename
                ).is_a_regex_pattern():
                    """
                    A regex pattern is recognized by the parentheses at the start and end of the target_basename string.

                    If a regex pattern is found, then the string inside of the parentheses contains the glob-path
                    for finding additional source dirnames from which files must be copied.

                    This glob-path may contain a wildcard (in angle brackets). The match for this wildcard is used
                    as the target_basename for the target node. If there is no wildcard, then the target_basename is set to the
                    basename of the string inside the parentheses.

                    For every match M of the glob pattern, a new TargetNode is created with source path M
                    and target_basename T, where T is the string that matches the wildcard. These target
                    nodes are added to the list of child nodes of the parent node, and processed recursively.
                    in the same way as the other simple child nodes.
                    """

                with it().processes_filename_patterns_and_resolves_to_actual_files():
                    """
                    The parse_target_node action processes the filename patterns in the target_node_json
                    and resolves them to concrete file paths. This includes:

                    1. Expanding glob patterns (e.g. "*.md", "**/*.py") to concrete file paths
                    2. Applying exclusion patterns (patterns that have false as their associated value)
                    3. Filtering files according to any ignore patterns

                    The resulting target_node will have filename_patterns that contain only
                    concrete file paths that should be copied, not patterns.
                    """

                with it().handles_directories_recursively():
                    """
                    If a filename pattern resolves to a directory, the parse_target_node_action
                    dynamically creates a new target node for that directory. This new target node
                    has '*' as its filename pattern so that the entire directory will be copied.

                    These dynamically created target nodes are then processed recursively just like
                    any other target node, which means their contents will be resolved to concrete
                    file paths before being passed to the copy_files action.

                    This approach ensures that directories are handled properly and that all files
                    within them are copied to the correct destination structure.
                    """

                assert r.target_node

            assert r.config.target_nodes

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
