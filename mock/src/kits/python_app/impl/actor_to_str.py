from sunya import actor_to_str
from sunya.utils.case import type_name_to_kebab

import kits.python_app.impl.entities as E


@actor_to_str.method((E.Function,))
def function_to_str(function):
    prefix = function.container + "->" if function.container else ""
    return f"{prefix}{function.name}+:function"


@actor_to_str.method((E.List,))
def list_to_str(list):
    return f"{list.name}+:list"


@actor_to_str.method((E.PythonModule,))
def module_to_str(module):
    return f"{type_name_to_kebab(module)}:module"


@actor_to_str.method((E.Form,))
def form_to_str(form):
    return f"{form.name}:form"


@actor_to_str.method((E.Enum,))
def enum_to_str(enum):
    return f"{type_name_to_kebab(enum)}:enum"
