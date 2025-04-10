from sunya import the, add_scenario, G as g, R as r, it

scenario_name = f"backend/ms2_lcopy_creates_the_target_nodes"


def start():
    with add_scenario(scenario_name):
        with (
            the(g.parse_config_file_action)
            .calls_the(g.parse_target_node_action)
            .with_a(r.target_node_json)
            .to_create_a(r.list_of_target_nodes)
        ):
            with (
                it()
                .returns_none_if_the(r.labels)
                .of_the_(r.target_node_json)
                .dont_match_with_the_labels_in_the(r.options)
            ):
                pass

            with it().may_determine_that_the(r.target_basename).is_a_regex_pattern():
                """
                A regex pattern is recognized by the parentheses at the start and end of the target_basename string.

                If a regex pattern is found, then the string inside of the parentheses contains the glob-path
                for finding additional source dirnames from which files must be copied. This glob-path contains
                a wildcard (in angle brackets). The match for this wildcard is used as the target_basename
                for the target node.

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

            with (
                it()
                .calls_the(r.create_target_node_action)
                .to_create_a(r.target_node)
                .based_on_the(r.target_node_json)
            ):
                assert r.target_node

            with it().may_call(r.parse_target_node_action).recursively():
                """
                When we use recursion to parse a simple target_node_json (without a regex pattern),
                then the source_dirname is the source directory of the parent node (we don't extend
                if with the target_basename).
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

            assert len(r.list_target_nodes)
