from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from .get_module_description_context import get_module_description_context
from .get_scenario_description_context import get_scenario_description_context


class PromptWriter:
    def __init__(self):
        templates_dir = Path(__file__).parent / "templates"
        self.templates_dir = Path(templates_dir).absolute()
        self.jinja_env = Environment(loader=FileSystemLoader(self.templates_dir))

    def get_module_description(self, module):
        context = get_module_description_context(module)
        return self._render_template("spec.md.j2", context)

    def get_scenario_description(self, scenario_name, scenario):
        context = get_scenario_description_context(scenario_name, scenario)
        return self._render_template("scenario.md.j2", context)

    def _render_template(self, fn, context):
        template = self.jinja_env.get_template(fn)
        rendered_template = template.render(context)
        return rendered_template
