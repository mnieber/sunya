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

notes_1 = """
The transaction_id is later used to call back to the frontend (using a server
event) to inform about the status of the plot creation.
"""

notes_2 = """
Every thread has its own instance of the domain_event_manager. The domain_event_manager
is created if it does not yet exist for the current thread.

The domain_event_manager is used as a Python context manager (using the 'with' statement).
When we enter the domain_event_manager context, we increase its reference count.
When the reference count goes to zero, we finalize the transaction and remove the
domain_event_manager instance from the thread storage.

Note that there is no database transaction that is associated with the domain event manager.
"""

notes_3 = """
The life-cycle events for the transaction are:
1. It implicitly exists via the domain events in memory
2. If we abort early then the transaction is rolled back and removed from memory
3. It is saved to the database as domain events in the pending state
4. The g.process_domain_events_action may abort and move the domain events to the rejected state
5. The g.process_domain_events_action may accept and move the domain events to the accepted state
"""

notes_4 = """
The creation of polygons and plot_questionnaires is not
based on domain events since they are just values.
"""

notes_5 = """
Clients can ask the domain event manager to append new domain events.
The transaction_id is automatically assigned to these new domain events.
The new domain events are stored in memory, and are inserted into the
domain event table at the end of the transaction.

When any client (of the domain event manager) reconstructs an entity by
replaying domain events, they will ask the domain event manager for the events.
They will receive all domain events up to the event_sequence_number (this is public data),
plus the new domain events that were created in the same transaction (this data is private
to the thread/transaction)
"""

notes_6 = """
When an action handles a call, it usually starts by reconstructing the entity from its domain events.
The reconstruction is done by both from the public events (up to the event_sequence_number in the transaction)
and the private events in the current transaction.

The action then verifies that the call is valid.
E.g. if the call says "rename plot from old-name to new-name", but the current name of the plot
is not "old-name" (someone else changed it in the meantime), then the action raises an exception
that aborts the transaction.

When the call is valid then the action calls the domain_event_manager to insert new domain events.
"""

notes_7 = """
When the client calls the create_domain_event action to create a new domain event
it includes the list of entity ids of the affected entities. The domain events and
associated entity ids are stored in the r.domain_event_manager.

The create_domain_event raises an exception if there is no current transaction in the
domain event manager.
"""


notes_8 = """
Note that the plot may have errors. However, these errors are always determined dynamically when
the plot is used. Therefore, we don't try to validate the plot at this point, but instead let
the user deal with plot errors in the frontend later when the plot is already created.
"""

notes_9 = """
The api request may contain a plot-list name that should be used instead of the default one.
Below we find the correct plot list, which is either the default one or the one specified in the api request.
"""

notes_10 = """
When observers of the transaction_id receive a callback, they will receive the id of the created plot.
"""

notes_11 = """
The g.insert_domain_events_action is called when the scope of the domain event manager context ends.
"""

notes_12 = """
The g.process_domain_events_action will load the domain evens wit the given transaction_id.
"""

notes_13 = """
The g.process_domain_events_loop is triggered at most twice per second. It runs in a single thread
(there are no concurrent executions). It will find the next pending transaction_id in the domain_events table
and call the g.process_domain_events_action to process these domain events.
It will mark the domain events as accepted and call back to the observers of the transaction_id
(such as the frontend).
"""


def start():
    with add_scenario(scenario_name):
        # create a plot in the project
        with goal(i.create_a(r.plot).in_the(r.project)):
            with the(g.frontend).calls_the(g.create_plot_api_view).with_a(
                r.transaction_id
            ):
                notes_1

                with it().calls_the(g.get_domain_event_manager_function).to_get_the(
                    r.domain_event_manager
                ).from_the(g.thread_storage):
                    notes_2

                    assert r.domain_event_manager

                    with (
                        the(r.domain_event_manager)
                        .when_it_is_first_entered_as_a_context()
                        .creates_a(r.transaction)
                        .with_the(r.transaction_id)
                        .and_the_current(r.event_sequence_number)
                    ):
                        notes_3

                    notes_4
                    notes_5

                    # Create the polygon
                    with (
                        it()
                        .calls_the(g.create_polygon_action)
                        .using_the(r.polygon)
                        .that_is_taken_from_the(r.api_request)
                    ):
                        assert r.polygon

                    # Add rollback action for the polygon
                    with (
                        it()
                        .adds_a(r.rollback_action)
                        .to_delete_the(r.polygon)
                        .to_the(r.domain_event_manager)
                    ):
                        pass

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

                    # Add rollback action for the plot_questionnaire
                    with (
                        it()
                        .adds_a(r.rollback_action)
                        .to_delete_the(r.plot_questionnaire)
                        .to_the(r.domain_event_manager)
                    ):
                        pass

                    # create the plot
                    with it().calls_the(g.create_plot_action):
                        notes_6

                        # insert domain events to create the plot
                        with (
                            it()
                            .calls_the(g.create_domain_event_action)
                            .several_times_to_create_new(r.domain_events)
                            .that_are_added_to_the(r.domain_event_manager)
                        ):
                            with (
                                the(g.create_domain_event_action)
                                .calls_the(g.get_domain_event_manager_function)
                                .to_get_the(r.domain_event_manager)
                                .from_the(g.thread_storage)
                            ):
                                assert r.domain_event_manager

                            notes_7

                            assert r.update_plot_fields_domain_event
                            assert r.update_plot_fields_domain_event.payload.plot_id
                            assert r.update_plot_owner_domain_event
                            assert r.update_plot_questionnaire_domain_event

                        with it().reconstructs_the_plot_with_id(r.plot_id):
                            assert r.plot

                        notes_8

                        # add the plot to the project
                        with goal(i.add_the(r.plot).to_the(r.project)):
                            with it().calls_the(g.add_plot_to_project_action):
                                notes_9

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

                        # return the plot-id
                        with it().returns_the_id_of_the_created(r.plot):
                            pass

                    with (
                        it()
                        .sets_the(r.transaction_payload)
                        .to_the_id_of_the_created(r.plot_id)
                    ):
                        notes_10

                # The domain event manager inserts the new domain events
                with it().calls_the(g.insert_domain_events_action):
                    notes_11

                    with (
                        it()
                        .locks_the(g.domain_event_table_semaphore)
                        .using_the(g.lock_semaphore_action)
                    ):
                        with it().saves_the(r.domain_events):
                            pass

                        with it().updates_the(g.entity_id_2_domain_event_id_table):
                            pass

                        with it().saves_the(r.transaction).to_the(g.transaction_table):
                            notes_12

            with the(g.process_domain_events_loop).calls_the(
                g.process_domain_events_action
            ):
                notes_13
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


from sunya import G as m
from sunya import G as r
from sunya import G as goals

diagram_1 = f"""
```mermaid
sequenceDiagram
    participant {m.External.Frontend}
    participant {m.Plots.ApiViews.CreatePlotApiView}
    participant {m.DomainEvents.Rules.GetDomainEventManager}
    participant {m.DomainEvents.Models.DomainEventManager}

    # 🟩 Create Plot
    {goals.note_over(r.Frontend, goal().create_a(r.plot).in_the(r.project))}

    # 🟧 Get Domain Event Manager
    {r.Frontend                          >> r.CreatePlotApiView}     : {g.calls(r.transaction_id)}
    Note over {r.CreatePlotApiView}      :  See [1]
    {r.CreatePlotApiView                 >> r.GetDomainEventManager} : {g.calls()}
    Note over {r.GetDomainEventManager}  :  See [2]
    {r.GetDomainEventManager             >> r.CreatePlotApiView}     : {g.returns(r.domain_event_manager)}

    # 🟧 Create a transaction by entering the Domain Event Manager context
    {r.CreatePlotApiView                 >> r.DomainEventManager}    : {g.enters_as_context()}
    {r.DomainEventManager                >> r.self}                  : {g.increases_reference_count()}
    {r.DomainEventManager                >> r.self}                  : {g.stores(r.event_sequence_number)}
    Note over {r.DomainEventManager}     :  See [3]

    # 🟧 Create the plot
    Note over {r.CreatePlotApiView} {r.note("See diagram 2 below for details of plot creation and creation of domain events.")}

    # 🟧 Finish CreatePlotApiView
    Note over {r.CreatePlotApiView}      :  See [10]
    {r.CreatePlotApiView                 >> r.DomainEventManager}    : {g.sets(r.transaction_payload).to(r.plot_id)}

    Note over {r.CreatePlotApiView} {r.note("See diagram 3 below for details of domain event insertion and processing.")}
```
"""

diagram_2 = f"""
```mermaid
sequenceDiagram
    participant {m.Plots.ApiViews.CreatePlotApiView}
    participant {m.Plots.Actions.CreatePolygon}
    participant {m.Plots.Actions.CreatePlotQuestionnaire}
    participant {m.Plots.Actions.CreatePlot}
    participant {m.Projects.Actions.AddPlotToProject}
    participant {m.DomainEvents.Models.DomainEventManager}

    # 🟩 Create Plot
    {goals.note_over(r.CreatePlotApiView, goal().create_a(r.plot))}

    # 🟧 Create polygon
    Note over {r.CreatePlotApiView}:  See [4]
    {r.CreatePlotApiView           >> r.CreatePolygon}           : {g.calls(r.polygon_data)}
    {r.CreatePolygon               >> r.self}                    : {g.creates(r.polygon)}
    {r.CreatePolygon               >> r.DomainEventManager}      : {g.adds(r.rollback_action).to_delete(r.polygon)}

    # 🟧 Create questionnaire
    {r.CreatePlotApiView           >> r.CreatePlotQuestionnaire} : {g.calls(r.questionnaire_data)}
    {r.CreatePlotQuestionnaire     >> r.self}                    : {g.validates_and_creates(r.plot_questionnaire)}
    {r.CreatePlotQuestionnaire     >> r.DomainEventManager}      : {g.adds(r.rollback_action).to_delete(r.plot_questionnaire)}

    # 🟧 Create plot with domain events
    {r.CreatePlotApiView           >> r.CreatePlot}              : {g.calls(r.create_plot_form)}
    Note over {r.CreatePlot}       :  See [5, 6, 7, 8]
    {r.CreatePlot                  >> r.DomainEventManager}      : {g.creates(r.update_plot_fields_domain_event)}
    {r.CreatePlot                  >> r.DomainEventManager}      : {g.creates(r.update_plot_owner_domain_event)}
    {r.CreatePlot                  >> r.DomainEventManager}      : {g.creates(r.update_plot_questionnaire_domain_event)}

    # 🟧 Add plot to project
    {r.CreatePlot                  >> r.AddPlotToProject}        : {g.calls(r.plot, r.project)}
    {r.AddPlotToProject            >> r.self}                    : {g.reconstructs(r.plot).from_events()}
    {r.AddPlotToProject            >> r.self}                    : {g.finds(r.plot_list).for_(r.project)}
    Note over {r.AddPlotToProject} :  See [9]
    {r.AddPlotToProject            >> r.DomainEventManager}      : {g.creates(r.add_plot_to_plot_list_domain_event)}
    {r.AddPlotToProject            >> r.CreatePlot}              : {g.returns()}

    # 🟧 Return plot id
    {r.CreatePlot                  >> r.CreatePlotApiView}       : {g.returns(r.plot_id)}
```
"""

diagram_3 = f"""
```mermaid
sequenceDiagram
    participant {m.External.Frontend}
    participant {m.DomainEvents.Actions.InsertDomainEvents}
    participant {m.DomainEvents.ProcessDomainEventsLoop}
    participant {m.DomainEvents.Models.DomainEventManager}

    # 🟩 Create Plot
    {goals.note_over(r.DomainEventManager, goal().process(r.domain_events))}

    # 🟧 Insert domain events
    Note over {r.DomainEventManager}     :  See [11]
    {r.DomainEventManager                >> r.InsertDomainEvents}    : {g.calls()}
    {r.InsertDomainEvents                >> r.self}                  : {g.locks(r.domain_event_table_semaphore)}
    {r.InsertDomainEvents                >> r.self}                  : {g.saves(r.domain_events)}
    {r.InsertDomainEvents                >> r.self}                  : {g.updates(r.entity_id_2_domain_event_id_table)}

    # 🟧 Background processing
    Note over {r.ProcessDomainEventsLoop}:  See [13]
    {r.ProcessDomainEventsLoop           >> r.self}                  : {g.processes_and_accepts_the(r.domain_events).for_the_next(r.transaction_id)}
    {r.ProcessDomainEventsLoop           >> r.Frontend}              : {g.notifies(r.transaction_id, r.plot_id)}
```
"""
