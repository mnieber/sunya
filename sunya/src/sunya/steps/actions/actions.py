from sunya.steps.models.rel import Rel
from sunya.steps.rules.rel_to_string import rel_to_string
from sunya.scenarios.models.scenario import get_scenario
from sunya.steps.actions.update_step_rel import update_step_rel


class Actions:
    def calls(self, *args, **kwargs):
        step = get_scenario().get_node().get_goal().get_step()
        update_step_rel(step, "calls", "with_args", args, kwargs)
        return f"calls({_get_format_str(args, kwargs)})"

    def returns(self, *args):
        step = get_scenario().get_node().get_goal().get_step()
        update_step_rel(step, "returns", "", args)
        return f"returns({_get_format_str(args, dict())})"

    def creates(self, *args):
        step = get_scenario().get_node().get_goal().get_step()
        update_step_rel(step, "creates", "", args)
        return f"creates({_get_format_str(args, dict())})"

    def it(self, rel: Rel):
        step = get_scenario().get_node().get_goal().get_step()
        step.rel = rel
        return rel_to_string(rel)


actions = Actions()


def _get_format_str(args, kwargs):
    formatted_args = ", ".join(str(arg) for arg in args)
    formatted_kwargs = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    infix = ", " if args and kwargs else ""
    format_str = formatted_args + infix + formatted_kwargs
    return format_str
