from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from .get_modules_description_context import get_modules_description_context
from .get_scenario_description_context import get_scenario_description_context


class PromptWriter:
    def __init__(self, scenario, module_order, prompts_dir):
        self.scenario = scenario
        self.module_order = module_order
        self.prompts_dir = Path(prompts_dir)
        self.jinja_env = Environment(loader=FileSystemLoader(self.prompts_dir))

    def get_highlevel_description(self):
        return self._render_template("1.highlevel-description.md.j2", dict())

    def get_modules_description(self):
        context = get_modules_description_context(
            self.scenario.entity_by_key.values(), self.module_order
        )
        return self._render_template("2.modules-description.md.j2", context)

    def get_scenario_description(self):
        context = get_scenario_description_context(self.scenario)
        return self._render_template("3.scenario-description.md.j2", context)

    def get_code_generation_instructions(self):
        context = get_modules_description_context(
            self.scenario.entity_by_key.values(), self.module_order
        )
        return self._render_template("archive-code-generation.md.j2", context)

    def _render_template(self, fn, context):
        template = self.jinja_env.get_template(fn)
        rendered_template = template.render(context)
        return rendered_template
