from mock.django_app.namespace import Action, DjangoModule
from sunya import Entity


class DomainEvents(DjangoModule):
    class Models:
        class DomainEvent(Entity):
            type_id: int
            payload = dict
            timestamp = int

        class DomainEventType(Entity):
            type_id: int
            type_name: str

        class Lock:
            lock_id: str

        class EntityId2DomainEventId:
            entity_id: str
            domain_event_id: str

    class Actions:
        class ProcessDomainEvents(Action):
            pass

        class UpdateViewTables(Action):
            pass
