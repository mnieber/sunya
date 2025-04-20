from kits.django_app.namespace import Action, DjangoModule, Rule
from kits.python_app.namespace import Form, Guid, Function
from sunya import Entity
import typing as T


class DomainEvents(DjangoModule):
    class Models:
        class DomainEvent(Entity):
            type_id: int
            payload = dict
            timestamp = int
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
            domain_events: T.List["DomainEvents.Models.DomainEvent"]
            domain_event_ids_by_entity_id: T.Dict[Guid, T.List[Guid]]

            def enter(self):
                pass

            def exit(self):
                pass

        class GetDomainEventManager(Function):
            pass
