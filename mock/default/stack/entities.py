from sunya import Entity, actor_to_str
from sunya.utils import type_name_to_kebab
from dataclassy import dataclass


class Module(Entity):
    pass


class Form(Entity):
    name: str
    data: dict = {}


@dataclass(kw_only=True)
class Value:
    pass


class Enum(Value):
    name: str


class JSON(Value):
    data: str = ""


class List(Entity):
    name: str
    items: list = []


class Function(Entity):
    name: str = ""

    def __post_init__(self):
        self.name = self.name or type_name_to_kebab(self)


@actor_to_str.method((Function,))
def function_to_str(function):
    return f"{function.name}+:function"


@actor_to_str.method((List,))
def list_to_str(list):
    return f"{list.name}+:list"


@actor_to_str.method((Module,))
def module_to_str(module):
    return f"{type_name_to_kebab(module)}:module"


@actor_to_str.method((Form,))
def form_to_str(form):
    return f"{form.name}:form"


@actor_to_str.method((Enum,))
def enum_to_str(enum):
    return f"{type_name_to_kebab(enum)}:enum"
