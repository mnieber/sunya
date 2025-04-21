from sunya import Entity
from kits.python_app.namespace import Function
from python_app.namespace import PythonModule


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
