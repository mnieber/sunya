from sunya import Entity, actor_to_str
from sunya.utils import type_name_to_kebab
from default.stack.namespace import Function


class Action(Function):
    pass


class Rule(Function):
    pass


class ApiView(Entity):
    pass


class Request(Entity):
    endpoint: str
    data: dict = {}


@actor_to_str.method((Action,))
def action_to_str(action):
    return f"{type_name_to_kebab(action)}:action"


@actor_to_str.method((Rule,))
def rule_to_str(rule):
    return f"{type_name_to_kebab(rule)}:rule"


@actor_to_str.method((ApiView,))
def api_view_to_str(api_view):
    return f"{type_name_to_kebab(api_view)}:api-view"


@actor_to_str.method((Request,))
def request_to_str(request):
    return f"{request.endpoint}:request"
