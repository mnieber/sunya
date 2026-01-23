from datetime import datetime

from sunya import Entity
from mock.entities.django_app.namespace import DjangoModule
from mock.entities.python_app.namespace import Form


class Database(DjangoModule):
    class Models:
        class Semaphore(Entity):
            name: str
            created_at: datetime

    class Actions:
        class CreateSemaphore:
            class Args:
                form: Form

        class CreateLock:
            class Args:
                semaphore_name: str
