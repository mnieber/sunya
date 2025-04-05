from sunya import Entity
from sunya.utils import type_name_to_kebab
from dataclassy import dataclass


class PythonModule(Entity):
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
    container: str = ""

    def __post_init__(self):
        self.name = self.name or type_name_to_kebab(self)


class Action(Function):
    pass
