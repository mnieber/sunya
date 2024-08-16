from sunya.utils import dict2yaml
from .get_module_description_context import get_module_description_context
from default.stack.prompt_writer.get_scenario_description_context import (
    get_scenario_description_context,
)


class PromptWriter:
    def get_module_spec(self, module):
        return dict2yaml(get_module_description_context(module))

    def get_scenario_description(self, scenario_name, scenario):
        return dict2yaml(get_scenario_description_context(scenario_name, scenario))
