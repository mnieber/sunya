# Module: database

## Database

```python
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
```

