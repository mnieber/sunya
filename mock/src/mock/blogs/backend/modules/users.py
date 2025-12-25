from sunya import Entity
from kits.django_app.impl.namespace import DjangoModule


class Users(DjangoModule):
    class Models:
        class User(Entity):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False
