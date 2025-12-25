from sunya import Entity
from kits.python_app.impl.namespace import Function
from kits.python_app.impl.namespace import PythonModule


class Action(Function):
    pass


class Model(Entity):
    pass


class DjangoModule(PythonModule):
    pass


class Rule(Function):
    pass


class ApiView(Entity):
    pass


class Request(Entity):
    endpoint: str
    data: dict = {}
