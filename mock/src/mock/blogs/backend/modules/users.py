from sunya import Entity
from mock.django_app.namespace import DjangoModule


class Users(DjangoModule):
    class Models:
        class User(Entity):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False
