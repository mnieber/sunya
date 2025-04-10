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

            with it().handles(r.directories).recursively():
                """
                If the file that must be copied is a directory, then parse_target_node dynamically adds a new
                TargetNode to the list of child nodes of the parent node. This new TargetNode
                has '*' as the sole entries in its list of filename patterns so that all files and subdirectories
                in the directory are copied. In this case, it uses recursion to parse the child nodes of the new TargetNode.
                """

            assert len(r.list_target_nodes)
