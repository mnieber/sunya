example_config = """
use-scenarios:
  instructions:
    .:
      - stack/prompts/general-explanation-of-technical-specifications.md
      - stack/prompts/structure-of-a-*.md
    blogs:
      .:
        - stack/roadmaps/roadmap.md

use-be-scenarios:
  instructions:
    blogs:
      backend:
        scenarios:
          (backend/scenarios/[scenario_name]):
            .:
              - scenario.py
              - steps.py
"""


def get_example_config_file():
    return example_config
