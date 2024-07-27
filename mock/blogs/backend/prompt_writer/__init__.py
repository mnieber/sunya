from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from sunya.utils.yaml import dict2yaml
from .get_module_description_context import get_module_description_context
from blogs.stack.prompt_writer.get_scenario_description_context import (
    get_scenario_description_context,
)


class PromptWriter:
    def __init__(self):
        templates_dir = Path(__file__).parent / "templates"
        self.templates_dir = Path(templates_dir).absolute()
        self.jinja_env = Environment(loader=FileSystemLoader(self.templates_dir))

    def get_module_spec(self, module):
        return dict2yaml(get_module_description_context(module))

    def get_scenario_description(self, scenario_fn, scenario):
        return dict2yaml(get_scenario_description_context(scenario_fn, scenario))

    def _render_template(self, fn, context):
        template = self.jinja_env.get_template(fn)
        rendered_template = template.render(context)
        return rendered_template
