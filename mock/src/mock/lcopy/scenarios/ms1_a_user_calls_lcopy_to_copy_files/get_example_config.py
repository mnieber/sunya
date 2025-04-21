from mock.lcopy.modules.configs import Configs


def get_example_config():
    """
    Returns an example Config instance that matches the structure in get_example_config_file.py
    """
    # Create the options
    options = Configs.Models.Options(
        destination="~/projects/sunya/res/claude/landler_be",
        concatenated_output_filename="~/projects/combined_output.txt",
        conflict="overwrite",
        verbose=True,
        purge=True,
        dry_run=False,
        default_ignore=True,
        extra_ignore=[".foo", ".tmp"],
        labels=["organize-dinner-party", "music-friends"],
    )

    # Create sources
    sources = {
        "app": Configs.Models.SourceConfig(
            path="/absolute/path/to/app",
            alias="app",
        ),
        "music-collection": Configs.Models.SourceConfig(
            path="/absolute/path/to/music",
            alias="music-collection",
        ),
    }

    # Create the main config
    example_config = Configs.Models.Config(
        source_dirname="/path/to/source",
        source_basename=".lcopy.yaml",
        sources=sources,
        options=options,
        target_nodes=[
            Configs.Models.TargetNode(
                target_basename="instructions",
                labels=["organize-dinner-party"],
                source_dirname="/path/to/source",
                filename_patterns=[],
                child_nodes=[
                    Configs.Models.TargetNode(
                        target_basename="recipes",
                        labels=["organize-dinner-party"],
                        source_dirname="/path/to/source",
                        filename_patterns=[
                            "/path/to/source/recipes/soups",
                            "/path/to/source/recipes/salads/green-salad.md",
                        ],
                        child_nodes=[],
                    ),
                    Configs.Models.TargetNode(
                        target_basename="music",
                        source_dirname="/path/to/source",
                        filename_patterns=[],
                        child_nodes=[
                            Configs.Models.TargetNode(
                                target_basename="jazz",
                                labels=["music-friends"],
                                source_dirname="/path/to/source",
                                filename_patterns=[
                                    "/path/to/source/music/jazz/song1.md"
                                ],
                                child_nodes=[],
                            ),
                            Configs.Models.TargetNode(
                                target_basename="rock",
                                source_dirname="/path/to/source",
                                filename_patterns=[],
                                child_nodes=[
                                    Configs.Models.TargetNode(
                                        target_basename="fragile",
                                        source_dirname="/path/to/source/music/rock/fragile/songs",
                                        filename_patterns=[
                                            "/path/to/source/music/rock/fragile/songs/track-01.md",
                                            "/path/to/source/music/rock/fragile/songs/track-02.md",
                                        ],
                                        child_nodes=[],
                                    ),
                                    Configs.Models.TargetNode(
                                        target_basename="close-to-the-edge",
                                        source_dirname="/path/to/source/music/rock/close-to-the-edge/songs",
                                        filename_patterns=[
                                            "/path/to/source/music/rock/close-to-the-edge/songs/track-01.md"
                                        ],
                                        child_nodes=[],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                includes=["app.documentation", "music-collection.playlists"],
            ),
            Configs.Models.TargetNode(
                target_basename="playlists",
                labels=["music-friends"],
                source_dirname="/path/to/source",
                filename_patterns=["/path/to/source/playlists/rock.md"],
                child_nodes=[],
            ),
            Configs.Models.TargetNode(
                target_basename="favorites",
                labels=["music-friends"],
                source_dirname="/path/to/source",
                filename_patterns=["/path/to/source/favorites/top10.txt"],
                child_nodes=[],
            ),
        ],
    )

    return example_config
