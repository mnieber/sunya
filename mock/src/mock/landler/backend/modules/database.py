from datetime import datetime

from sunya import Entity
from kits.django_app.impl.namespace import DjangoModule
from kits.python_app.impl.namespace import Form


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
