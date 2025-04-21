                    # The process_domain_events_action updates the models
                    with the(g.process_domain_events_action).locks_the(
                        r.process_domain_events_semaphore
                    ):
                        """
                        Note that if another process has to wait for the lock, then there is a good chance
                        that the domain events for that other process are already being processed by the
                        ongoing process. Therefore, this lock does not degrade the performance.
                        """
                        with (
                            it()
                            .determines_the(r.list_of_pending_domain_events)
                            .and_related_entries_in_the(
                                g.entity_id_2_domain_event_id_table
                            )
                        ):
                            """
                            The process_domain_events_action keeps track of the last domain event it processed.
                            Since the domain events and entity_id_2_domain_event_id entries are append-only,
                            it's easy to find out which domain events and entity_id_2_domain_event_id entries
                            must be processed.
                            """
                            assert r.list_of_pending_domain_events
                            assert r.entity_id_2_domain_event_id_map

                        with (
                            it()
                            .loops_over_the(r.list_of_pending_domain_events)
                            .chunked_by_the(r.transaction_id)
                        ):
                            with it().replays_all_events_on_each_related(r.entity):
                                with it().calls_the(g.save_function).on_the(r.plot):
                                    with (
                                        it()
                                        .permits_to_save_the(r.event_sourced_fields)
                                        .only_in_the_context_of_the(
                                            g.process_domain_events_action
                                        )
                                    ):
                                        """
                                        The save_function uses the direct_fields attribute of the meta
                                        class to determine which fields may be saved directly (e.g. in the django
                                        admin). Fields that are not direct fields may only be saved in the context
                                        of the processing a update_direct_fields domain_event.

                                        Note that events for event_sourced fields may also not update the
                                        direct fields. This is because direct fields should not be updated
                                        when the events are replayed.
                                        """

                            with (
                                it()
                                .marks_all(r.domain_events)
                                .for_the_(r.transaction_id)
                                .as_rejected_or_accepted()
                            ):
                                """
                                If any domain event was rejected, than all domain events for that transaction_id
                                are rejected."""

                            with it().calls_the(g.notify_transaction_observers_action):
                                pass


                """
                At this point we've updated the models, but we've not yet updated the
                view-tables.
                """




                                with it().calls_the(r.validate_plot_action):
                                    with it().validates_the(r.plot).in_the(r.plot_list):
                                        assert r.plot.errors or not r.plot.errors
