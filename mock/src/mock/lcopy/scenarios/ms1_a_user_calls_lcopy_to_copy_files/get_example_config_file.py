example_config_file = """
include_fns:
  - ../app/.lcopy.yaml

targets:
  instructions:
    __labels__: [organize-dinner-party]
    recipes:
      .:
        - recipes/soups
        - recipes/salads/green-salad.md
    music:
      jazz:
        __labels__: [music-friends]
        .:
          - music/jazz/*.md
      rock:
        (album-name):
          __source__: music/rock/<album-name>/songs
          .:
            - greatest-hits-of-*.md
"""


def get_example_config_file():
    return example_config_file
