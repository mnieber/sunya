example_config_file = """
include_fns:
  - ../app/.lcopy.yaml

targets:
  organize-dinner-party:
    instructions:
      recipes:
        "recipes/soups": true
        "recipes/salads/green-salad.md": true
      music:
        jazz:
          "music/jazz/*.md": true
        rock:
          (music/rock/<album-name>/songs):
            "greatest-hits-of-*.md": true
            "greatest-hits-of-me.md": false
"""


def get_example_config_file():
    return example_config_file
