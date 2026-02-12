from sunya import Entity
from sunya_mock.entities.python_app.namespace import Function
from sunya_mock.entities.python_app.namespace import PythonPackage


class Action(Function):
    pass


class Model(Entity):
    pass


class DjangoModule(PythonPackage):
    pass


class Rule(Function):
    pass


class ApiView(Entity):
    pass


class Request(Entity):
    endpoint: str
    data: dict = {}
