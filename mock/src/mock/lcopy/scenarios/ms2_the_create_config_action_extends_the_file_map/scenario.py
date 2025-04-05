from sunya import the, add_scenario, G as g, R as r, it

scenario_name = f"backend/ms2_the_create_config_action_extends_the_file_map"


def start():
    with add_scenario(scenario_name):
        with the(g.lcopy_tool).calls_the(g.process_config_action).with_a(
            r.config
        ).to_extend_the(r.filemap_tree):
            with (
                it()
                .adds_a(r.filemap_node)
                .for_every(r.target_directory)
                .in_the(r.root_config_node)
            ):
                with it().may_encounter_a(r.regex_pattern).in_the(r.target_directory):
                    """
                    A regex pattern is recognized by the parentheses at the start and end of the pattern string.
                    The variable part of the regex pattern is enclosed in square brackets.

                    The regex pattern is joined with the source directory to create a glob pattern.

                    For every match M of the glob pattern, a new config-node is created with source path M
                    and target subdirectory T, where T is the variable part of the regex pattern. This config-node is
                    then processed recursively as a "simple target directory".
                    """

                with it().otherwise_processes_the_simple(r.target_directory):
                    """
                    If there is no regex pattern, the target directory is processed as a simple directory.
                    """
                    with (
                        it()
                        .determines_the(r.list_of_exclude_patterns)
                        .in_the(r.target_directory)
                        .of_the(r.config)
                    ):
                        """
                        If a file or directory must be excluded from the destination directory, then its pattern
                        is prefixed with an exclamation mark.
                        """
                        assert r.list_of_exclude_patterns

                    with (
                        it()
                        .determines_the(r.list_of_filenames)
                        .in_the(r.target_directory)
                        .of_the(r.config)
                        .and_adds_them_to_the(r.filemap_node)
                    ):
                        """
                        The list of filenames is found by using the filename patterns in the config node. Filenames that
                        match one of the ignore patterns or one of the exclude patterns are ignored.
                        """

            assert len(r.filemap_tree)
