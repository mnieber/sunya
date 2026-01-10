# Module: domain_events

## DomainEvents

```python
class DomainEvents(DjangoModule):
    class Models:
        class DomainEvent(Entity):
            type_id: int
            payload: Any = dict
            timestamp: Any = int
            transaction_id: Guid

        class DomainEventType(Entity):
            type_id: int
            type_name: str

        class EntityId2DomainEventId:
            entity_id: str
            domain_event_id: str

        class Transaction(Entity):
            payload: dict
            rollback_handlers: dict

    class Actions:
        class CreateDomainEvent(Action):
            class Args:
                create_domain_event_form: Form
                entity_ids: list[Guid]

        class ProcessDomainEvents(Action):
            pass

        class UpdateViewTables(Action):
            pass

    class Rules:
        class ReconstructEntity(Rule):
            class Args:
                entity_id: str

    class Utils:
        class DomainEventManager:
            create_transaction_form: Form
            domain_events: T.List['DomainEvents.Models.DomainEvent']
            domain_event_ids_by_entity_id: T.Dict[Guid, T.List[Guid]]

        class GetDomainEventManager(Function):
            pass
```

