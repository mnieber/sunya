from sunya import (
    add_scenario,
    get_scenario,
    the,
    it,
    G as g,
    R as r,
)

scenario_name = f"backend/mrd5_a_user_adds_a_plot_to_a_project"


def process_domain_events():
    with add_scenario("backend/process_domain_events"):
        with the(g.process_domain_events_loop).calls_the(
            g.process_domain_events_action
        ):
            # Lock the domain events for processing
            with (
                it()
                .calls_the(g.lock_semaphore_action)
                .to_lock_the(r.process_domain_events_semaphore)
            ):
                """
                This lock prevents simultaneous instances of the process_domain_events_action.
                """

            """
            The process_domain_events_action is responsible for processing all new domain events
            that have been inserted but not yet processed. It works on batches of domain events
            that share the same transaction_id.
            """

            # Find the next batch of domain events to process
            with it().finds_the_next_unprocessed(r.transaction_batch):
                """
                The next unprocessed transaction batch consists of all domain events that:
                1. Have status = 0 (pending)
                2. Share the same transaction_id
                3. Have the earliest timestamp among all pending transactions

                This ensures we process transactions in the order they were created.
                """
                assert r.transaction_batch.domain_events
                assert r.transaction_batch.transaction_id
                assert (
                    r.transaction_batch.entity_ids
                )  # List of entity IDs affected by this transaction

            # Validate all domain events in the transaction
            with it().calls_the(g.validate_domain_events_action):
                """
                The validate_domain_events_action reconstructs each affected entity using:
                1. All domain events with timestamp <= transaction batch timestamp
                2. The pending domain events in the current transaction

                It applies validation rules to each domain event during replay.
                """

                # For each affected entity in the transaction
                for entity_id in r.transaction_batch.entity_ids:
                    r.current_entity_id = entity_id

                    # Determine entity type from the entity_id
                    with it().determines_the(r.entity_type).from_the(
                        r.current_entity_id
                    ):
                        pass

                    # Reconstruct the entity by replaying events
                    with (
                        it()
                        .reconstructs_the(r.entity)
                        .by_replaying_the(r.domain_events)
                        .with_timestamp_less_than_or_equal_to(
                            r.transaction_batch.timestamp
                        )
                        .that_affect_the(r.current_entity_id)
                    ):
                        """
                        This reconstruction process:
                        1. Starts with a blank entity
                        2. Applies all domain events in timestamp order

                        During replay, each domain event is validated to ensure it can be applied.
                        If any domain event fails validation, the entire transaction is marked invalid.
                        """
                        with (
                            it()
                            .marks_all(r.domain_events)
                            .in_the(r.transaction_batch)
                            .as_either_accepted_or_rejected()
                        ):
                            """
                            If some domain events are invalid, then all domain events in the transaction
                            are marked as invalid.
                            """

                        # Call cleanup handlers for rejected transaction
                        with (
                            it()
                            .calls_the(r.transaction_batch.cleanup_handlers)
                            .if_the_transaction_was_rejected()
                        ):
                            """
                            Cleanup handlers remove any dangling value objects that were created
                            during the transaction but should be deleted because the transaction
                            was rejected.
                            """

                        # Save the reconstructed entity if transaction was accepted
                        with (
                            it()
                            .saves_the(r.reconstructed_entity)
                            .if_the_transaction_was_accepted()
                        ):
                            """
                            The reconstructed entity is saved to the database.
                            """

            # If transaction was valid, update the model tables
            if r.transaction_batch.is_valid:
                # Update any view tables affected by this transaction
                with it().calls_the(g.update_view_tables_action):
                    """
                    The update_view_tables_action updates all view tables that depend on:
                    1. The entity types that were modified
                    2. The specific domain event types that were processed

                    Each view table updater declares which entity types and domain event types
                    it's interested in, and only gets called if relevant changes occurred.
                    """

                    # Find all view table updaters relevant to this transaction
                    with it().finds_all(r.relevant_view_updaters).for_the(
                        r.transaction_batch
                    ):
                        pass

                    # For each relevant view updater
                    for view_updater in r.relevant_view_updaters:
                        r.current_view_updater = view_updater

                        # Call the view updater with the updated models and domain events
                        with (
                            it()
                            .calls_the(r.current_view_updater)
                            .with_the(r.updated_models)
                            .and_the(r.transaction_batch.domain_events)
                        ):
                            """
                            Each view updater can decide whether to:
                            1. Update the view based on the domain events directly
                            2. Rebuild part of the view based on the updated models
                            """

            # Notify observers about the transaction completion
            with it().calls_the(g.notify_transaction_observers_action):
                """
                This notifies all observers that registered interest in this transaction_id,
                such as the frontend that initiated the action.

                The notification includes:
                1. The transaction_id
                2. Whether the transaction was successful
                3. The transaction payload (e.g., the ID of the created entity)
                4. Any error information if the transaction failed
                """

                # Find all observers for this transaction
                with (
                    it()
                    .notifies_all(r.observers)
                    .for_the(r.transaction_batch.transaction_id)
                ):
                    pass

            # Release the lock on the transaction batch
            with it().releases_the_lock_on(r.transaction_batch):
                pass

    return get_scenario("backend/process_domain_events")


def run():
    return process_domain_events()


if __name__ == "__main__":
    run()
