import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"mrd6_domain_events_are_processed")


def run_scenario():
    r.process_domain_events_loop = m.DomainEvents.ProcessDomainEventsLoop
    r.process_domain_events_action = m.DomainEvents.Actions.ProcessDomainEvents
    r.lock_semaphore_action = m.DomainEvents.Actions.LockSemaphore
    r.validate_domain_events_action = m.DomainEvents.Actions.ValidateDomainEvents
    r.update_view_tables_action = m.DomainEvents.Actions.UpdateViewTables
    r.notify_transaction_observers_action = m.DomainEvents.Actions.NotifyTransactionObservers

    with goal().process_pending(r.domain_events):
        # Process domain events
        with the(r.process_domain_events_loop).calls(r.process_domain_events_action):
            # Lock the domain events for processing
            with it().calls(r.lock_semaphore_action).to_lock_the(r.process_domain_events_semaphore):
                pass

            # Find the next batch of domain events to process
            with it().finds_the_next_unprocessed(r.transaction_batch):
                pass

            # Validate all domain events in the transaction
            with it().calls(r.validate_domain_events_action):
                # For each affected entity
                with it().determines_the(r.entity_type).from_the(r.entity_id):
                    pass

                # Reconstruct entity by replaying events
                with it().reconstructs_the(r.entity).by_replaying_the(r.domain_events):
                    with it().marks_all(r.domain_events).as_either_accepted_or_rejected():
                        pass

                    # Call cleanup handlers for rejected transaction
                    with it().calls_the(r.cleanup_handlers).if_the_transaction_was_rejected():
                        pass

                    # Save the reconstructed entity if transaction was accepted
                    with it().saves_the(r.reconstructed_entity).if_the_transaction_was_accepted():
                        pass

            # Update view tables if transaction was valid
            with it().calls(r.update_view_tables_action).if_transaction_valid():
                with it().finds_all(r.relevant_view_updaters).for_the(r.transaction_batch):
                    pass

                # Call each view updater
                with it().calls_each(r.view_updater).with_the(r.updated_models).and_the(r.domain_events):
                    pass

            # Notify observers about transaction completion
            with it().calls(r.notify_transaction_observers_action):
                with it().notifies_all(r.observers).for_the(r.transaction_id):
                    pass

            with it().releases_the_lock_on(r.transaction_batch):
                pass


markdown_node = sunya.add_markdown_node(scenario, "Domain events are processed")

markdown_node.markdown = """
The system processes pending domain events in batches by transaction ID. It validates events by reconstructing entities, updates view tables, and notifies observers. This scenario describes the background processing loop that ensures eventual consistency of the domain event system.

### Steps

#### It locks and finds the next transaction batch

The process domain events loop calls the `ProcessDomainEvents` action.</br>

**Note [1]**: This lock prevents simultaneous instances of the process_domain_events_action. Only one batch of domain events can be processed at a time.</br>

The action locks the process domain events semaphore to prevent concurrent processing.</br>

**Note [2]**: The process_domain_events_action is responsible for processing all new domain events that have been inserted but not yet processed. It works on batches of domain events that share the same transaction_id.</br>

**Note [3]**: The next unprocessed transaction batch consists of all domain events that: 1) Have status = 0 (pending), 2) Share the same transaction_id, 3) Have the earliest timestamp among all pending transactions. This ensures we process transactions in the order they were created.</br>

The action finds the next unprocessed transaction batch.</br>
The transaction batch contains the domain_events, transaction_id, and a list of entity IDs affected by this transaction.</br>

#### It validates domain events by reconstructing entities

**Note [4]**: The validate_domain_events_action reconstructs each affected entity using: 1) All domain events with timestamp <= transaction batch timestamp, 2) The pending domain events in the current transaction. It applies validation rules to each domain event during replay.</br>

The action calls `ValidateDomainEvents` to reconstruct each affected entity by replaying events.</br>

For each entity_id in the transaction batch, the action determines the entity type from the entity_id.</br>

**Note [5]**: This reconstruction process: 1) Starts with a blank entity, 2) Applies all domain events in timestamp order. During replay, each domain event is validated to ensure it can be applied. If any domain event fails validation, the entire transaction is marked invalid.</br>

The action reconstructs the entity by replaying all domain events (with timestamp <= transaction batch timestamp) that affect this entity_id.</br>

**Note [6]**: If some domain events are invalid, then all domain events in the transaction are marked as invalid. This is an all-or-nothing approach.</br>

During replay, events are validated and marked as either accepted or rejected.</br>

**Note [7]**: Cleanup handlers remove any dangling value objects that were created during the transaction but should be deleted because the transaction was rejected. For example, polygons or questionnaires that were created before domain event validation failed.</br>

If rejected, cleanup handlers are called to remove dangling value objects.</br>

**Note [8]**: The reconstructed entity is saved to the database. This updates the entity's state based on the accepted domain events.</br>

If accepted, the reconstructed entity is saved to the database.</br>

#### It updates views and notifies observers

**Note [9]**: The update_view_tables_action updates all view tables that depend on: 1) The entity types that were modified, 2) The specific domain event types that were processed. Each view table updater declares which entity types and domain event types it's interested in, and only gets called if relevant changes occurred.</br>

If the transaction was valid, the action calls `UpdateViewTables` to update all relevant view tables.</br>
The action finds all relevant view updaters for this transaction batch.</br>

**Note [10]**: Each view updater can decide whether to: 1) Update the view based on the domain events directly, 2) Rebuild part of the view based on the updated models.</br>

For each view updater, the action calls it with the updated models and domain events.</br>

**Note [11]**: This notifies all observers that registered interest in this transaction_id, such as the frontend that initiated the action. The notification includes: 1) The transaction_id, 2) Whether the transaction was successful, 3) The transaction payload (e.g., the ID of the created entity), 4) Any error information if the transaction failed.</br>

The action calls `NotifyTransactionObservers` to notify all observers of the transaction ID.</br>
The action finds all observers for this transaction and notifies them.</br>
The action releases the lock on the transaction batch.</br>

### Diagram

```mermaid
sequenceDiagram
    participant ProcessDomainEventsLoop as ProcessDomainEventsLoop
    participant ProcessDomainEvents as ProcessDomainEvents (action)
    participant LockSemaphore as LockSemaphore (action)
    participant ValidateDomainEvents as ValidateDomainEvents (action)
    participant UpdateViewTables as UpdateViewTables (action)
    participant NotifyTransactionObservers as NotifyTransactionObservers (action)

    Note over ProcessDomainEventsLoop,ProcessDomainEvents: Process Domain Events
    ProcessDomainEventsLoop->>ProcessDomainEvents: process_domain_events()

    Note over ProcessDomainEvents: See [1]
    ProcessDomainEvents->>LockSemaphore: lock_semaphore(process_domain_events_semaphore)

    Note over ProcessDomainEvents: See [2, 3]
    ProcessDomainEvents->>ProcessDomainEvents: find next unprocessed transaction batch

    Note over ProcessDomainEvents: See [4]
    ProcessDomainEvents->>ValidateDomainEvents: validate_domain_events(transaction_batch)

    loop for each affected entity
        Note over ValidateDomainEvents: See [5]
        ValidateDomainEvents->>ValidateDomainEvents: determine entity type from entity ID
        ValidateDomainEvents->>ValidateDomainEvents: reconstruct entity by replaying events

        Note over ValidateDomainEvents: See [6]
        ValidateDomainEvents->>ValidateDomainEvents: mark domain events as accepted or rejected

        alt transaction rejected
            Note over ValidateDomainEvents: See [7]
            ValidateDomainEvents->>ValidateDomainEvents: call cleanup handlers
        else transaction accepted
            Note over ValidateDomainEvents: See [8]
            ValidateDomainEvents->>ValidateDomainEvents: save reconstructed entity
        end
    end

    alt transaction valid
        Note over ProcessDomainEvents: See [9]
        ProcessDomainEvents->>UpdateViewTables: update_view_tables(transaction_batch)
        UpdateViewTables->>UpdateViewTables: find relevant view updaters
        loop for each view updater
            Note over UpdateViewTables: See [10]
            UpdateViewTables->>UpdateViewTables: call view updater with updated models and events
        end
    end

    Note over ProcessDomainEvents: See [11]
    ProcessDomainEvents->>NotifyTransactionObservers: notify_transaction_observers(transaction_id)
    NotifyTransactionObservers->>NotifyTransactionObservers: notify all observers

    ProcessDomainEvents->>ProcessDomainEvents: release lock on transaction batch
```
"""
