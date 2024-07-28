from sunya import Entity, Value, actor_to_str
from sunya.utils import type_name_to_kebab


class Module(Entity):
    pass


class Form(Entity):
    name: str
    data: dict = {}


class Enum(Value):
    name: str


class JSON(Value):
    data: str = ""


@actor_to_str.method((Module,))
def module_to_str(module):
    return f"{type_name_to_kebab(module)}:module"


@actor_to_str.method((Form,))
def form_to_str(form):
    return f"{form.name}:form"


@actor_to_str.method((Enum,))
def enum_to_str(enum):
    return f"{type_name_to_kebab(enum)}:enum"
