from mock.lcopy.modules.configs import Configs

example_config = Configs.Models.Config(
    source_dirname="/path/to/source",
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
                    filename_patterns=["recipes/soups" "recipes/salads/green-salad.md"],
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
                            filename_patterns=["music/jazz/*.md"],
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
                                    filename_patterns=["track-*.md"],
                                    child_nodes=[],
                                ),
                                Configs.Models.TargetNode(
                                    target_basename="close-to-the-edge",
                                    source_dirname="/path/to/source/music/rock/close-to-the-edge/songs",
                                    filename_patterns=["track-*.md"],
                                    child_nodes=[],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


def get_example_config():
    return example_config
