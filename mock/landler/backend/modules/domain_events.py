from default.stack.namespace import Module
from default.backend.namespace import Action
from sunya import EntityWithId, Entity, actor_to_str, G as g


class DomainEvents(Module):
    class Models:
        class DomainEvent(EntityWithId):
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


g.process_domain_events_action = DomainEvents.Actions.ProcessDomainEvents()
g.update_view_tables_action = DomainEvents.Actions.UpdateViewTables()


@actor_to_str.method((DomainEvents.Models.DomainEvent,))
def domain_event_to_str(domain_event):
    return f"{domain_event.type_id}-{domain_event.timestamp}+:domain_event"
