from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
    G as g,
    I as i,
    R as r,
)

scenario_name = f"backend/mrd5_a_user_adds_a_plot_to_a_project"


def start():
    with add_scenario(scenario_name):
        # create a plot in the project
        with goal(i.create_a(r.plot).in_the(r.project)):
            with the(g.frontend).calls_the(g.create_plot_api_view).with_a(
                r.transaction_id
            ):
                """
                The transaction_id is later used to call back to the frontend (using a server
                event) to inform about the status of the plot creation.
                """
                with (
                    it()
                    .uses_the(r.domain_event_manager_function)
                    .to_create_a(r.domain_manager_context)
                    .with_the(r.transaction_id)
                ):
                    with (
                        the(r.domain_event_manager_function)
                        .instantiates_the(r.domain_event_manager)
                        .in_the_(g.thread_storage)
                    ):
                        """
                        Every thread has its own instance of the domain_event_manager.
                        We also store the reference count to this domain_event_manager instance.
                        When there are nested calls to the domain_event_manager function, we
                        increment the reference count. When the reference count goes to zero,
                        we remove the domain_event_manager instance from the thread storage.
                        """

                    """
                    The domain event manager stores the the transaction_id and the
                    timestamp N of the plot creation, where N stands for "now".

                    Clients can ask the domain event manager to append new domain events.
                    The transaction_id is automatically assigned to these new domain events.
                    The new domain events are stored in memory, and are inserted into the
                    domain event table at the end of the transaction.

                    When any client reconstructs an entity by replaying domain events,
                    they will ask the domain event manager for the events. They will receive
                    all domain events up to the timestamp N, plus the new domain events that
                    were created in the same transaction.
                    """
                    # Note that the creation (below) of polygons and plot_questionnaires is not
                    # based on domain events since they are just values.

                    # Create the polygon
                    with (
                        it()
                        .calls_the(g.create_polygon_action)
                        .using_the(r.polygon)
                        .that_is_taken_from_the(r.api_request)
                    ):
                        assert r.polygon

                    # create the plot questionnaire
                    with it().calls_the(r.create_plot_questionnaire_action):
                        with (
                            it()
                            .calls_the(g.get_errors_in_plot_questionnaire_values_rule)
                            .to_validate_the_values_in_the(
                                g.create_plot_questionnaire_form
                            )
                            .against_the(g.plot_questionnaire_schema)
                        ):
                            pass

                        assert r.plot_questionnaire

                    # create the plot
                    with it().calls_the(g.create_plot_action):
                        # insert domain events to create the plot
                        with (
                            it()
                            .calls_the(g.create_domain_event_action)
                            .several_times_to_create_new(r.domain_events)
                            .that_are_added_to_the(r.domain_event_manager)
                        ):
                            with (
                                the(g.create_domain_event_action)
                                .calls_the(g.get_event_manager_function)
                                .to_get_the(r.domain_event_manager)
                                .from_the(g.thread_storage)
                            ):
                                assert r.domain_event_manager

                            """
                            The call to the create_domain_event action includes the list of entity
                            ids of the affected entities. The domain events and associated entity ids
                            are stored in the r.domain_event_manager.

                            The create_domain_event raises an exception if there is no current
                            domain event manager context.
                            """
                            assert r.update_plot_fields_domain_event
                            assert r.update_plot_fields_domain_event.payload.plot_id
                            assert r.update_plot_owner_domain_event
                            assert r.update_plot_questionnaire_domain_event

                        with it().reconstructs_the_plot_with_id(r.plot_id):
                            assert r.plot

                        # add the plot to the project
                        with goal(i.add_the(r.plot).to_the(r.project)):
                            with it().calls_the(g.add_plot_to_project_action):
                                """
                                The api request may contain a plot-list name that should be used
                                instead of the default one.
                                """
                                with it().finds_the_target(r.plot_list).for_the(
                                    r.project
                                ):
                                    assert r.plot_list

                                with (
                                    it()
                                    .calls_the(g.create_domain_event_action)
                                    .to_insert_a(r.add_plot_to_plot_list_domain_event)
                                ):
                                    pass

                        """
                        Note that the plot may have errors. However, these errors are always
                        determined dynamically when the plot is used. Therefore, we don't try
                        to validate the plot at this point, but instead let the user deal with
                        plot errors in the frontend later when the plot is already created.
                        """

                        # return the plot-id
                        with it().returns_the_id_of_the_created(r.plot):
                            pass

                    with (
                        it()
                        .sets_the(r.transaction_payload)
                        .to_the_id_of_the_created(r.plot_id)
                        .and_sets_the(r.transaction_rollback_handler)
                        .to_clean_up_the_polygon_and_questionnaire()
                    ):
                        """
                        When observers of the transaction_id receive a callback, they will
                        receive the id of the created plot.

                        If the transaction is rolled back, the polygon and questionnaire are deleted
                        by the rollback handler.
                        """

                # The domain event manager inserts the new domain events
                with it().calls_the(g.insert_domain_events_action):
                    """
                    The g.insert_domain_events_action is called when the scope of the
                    domain event manager context ends.
                    """
                    with (
                        it()
                        .locks_the(g.domain_event_table_semaphore)
                        .using_the(g.lock_semaphore_action)
                    ):
                        with (
                            it()
                            .replays_the(r.domain_events)
                            .that_are_in_memory()
                            .to_catch_problems_early_and_abort_if_necessary()
                        ):
                            pass

                        with it().saves_the(r.domain_events):
                            pass

                        with it().updates_the(g.entity_id_2_domain_event_id_table):
                            pass

                        with it().saves_the(r.transaction).to_the(g.transaction_table):
                            """
                            The g.process_domain_events_action will load the transaction from the
                            g.transaction_table.
                            """

            with the(g.process_domain_events_loop).calls_the(
                g.process_domain_events_action
            ):
                """
                The g.process_domain_events_loop is triggered twice per second. It will call
                the g.process_domain_events_action to process all new domain events and will
                call back to the observers of the transaction_id (such as the frontend).

                Note that the g.process_domain_events_action may still reject all domain events
                for the transaction. The domain events only become official when they are moved
                to the 'accepted' state by the g.process_domain_events_action.
                """
                assert r.plot.polygon == r.polygon
                assert r.plot.owner == g.user_session.active_organization

    return get_scenario(scenario_name)


def run():
    from ..mrd4_a_user_creates_a_project import scenario as mrd4_scenario

    run_scenario(mrd4_scenario)
    assert r.project

    return start()


if __name__ == "__main__":
    run()
