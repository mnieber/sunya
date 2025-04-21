from sunya import actor_to_str
from sunya.utils.case import type_name_to_kebab

import kits.django_app.impl.entities as E


@actor_to_str.method((E.Action,))
def action_to_str(action):
    return f":action"


@actor_to_str.method((E.ApiView,))
def api_view_to_str(api_view):
    return f":api_view"


@actor_to_str.method((E.Rule,))
def rule_to_str(rule):
    return f"{type_name_to_kebab(rule)}:rule"


@actor_to_str.method((E.Request,))
def request_to_str(request):
    return f"{request.endpoint}:request"


@actor_to_str.method((E.Model,))
def model_to_str(model):
    return f"{type_name_to_kebab(model)}:model"
