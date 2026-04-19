import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"mrd5_a_user_adds_a_plot_to_a_project")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.create_plot_api_view = m.Plots.ApiViews.CreatePlotApiView
    r.get_domain_event_manager_function = m.DomainEvents.Rules.GetDomainEventManager
    r.domain_event_manager = m.DomainEvents.Models.DomainEventManager
    r.create_polygon_action = m.Plots.Actions.CreatePolygon
    r.create_plot_questionnaire_action = m.Plots.Actions.CreatePlotQuestionnaire
    r.create_plot_action = m.Plots.Actions.CreatePlot
    r.create_domain_event_action = m.DomainEvents.Actions.CreateDomainEvent
    r.add_plot_to_project_action = m.Projects.Actions.AddPlotToProject
    r.insert_domain_events_action = m.DomainEvents.Actions.InsertDomainEvents
    r.process_domain_events_loop = m.DomainEvents.ProcessDomainEventsLoop
    r.process_domain_events_action = m.DomainEvents.Actions.ProcessDomainEvents

    with goal().create_a(r.plot).in_the(r.project):
        # Create a plot in the project
        with the(r.frontend).calls(r.create_plot_api_view).with_a(r.transaction_id):
            # Get domain event manager
            with it().calls(r.get_domain_event_manager_function).to_get_the(r.domain_event_manager):
                pass

            # Enter domain event manager context
            with the(r.domain_event_manager).when_entered_as_context().creates_a(r.transaction):
                pass

            # Create the polygon
            with it().calls(r.create_polygon_action).with_the(r.polygon_data):
                it().creates(r.polygon)
                it().adds(r.rollback_action).to_delete(r.polygon).to_the(r.domain_event_manager)

            # Create the plot questionnaire
            with it().calls(r.create_plot_questionnaire_action):
                it().validates_and_creates(r.plot_questionnaire)
                it().adds(r.rollback_action).to_delete(r.plot_questionnaire).to_the(r.domain_event_manager)

            # Create the plot using domain events
            with it().calls(r.create_plot_action):
                # Insert domain events
                with it().calls(r.create_domain_event_action).several_times():
                    it().creates(r.update_plot_fields_domain_event)
                    it().creates(r.update_plot_owner_domain_event)
                    it().creates(r.update_plot_questionnaire_domain_event)

                it().reconstructs_the_plot_with_id(r.plot_id)

                # Add plot to project
                with it().calls(r.add_plot_to_project_action):
                    it().finds_the_target(r.plot_list).for_the(r.project)
                    it().creates(r.add_plot_to_plot_list_domain_event)

                it().returns_the_id_of_the_created(r.plot)

            it().sets_the(r.transaction_payload).to_the_id_of_the_created(r.plot_id)

            # Insert domain events to database
            with it().calls(r.insert_domain_events_action):
                it().locks_the(r.domain_event_table_semaphore)
                it().saves_the(r.domain_events)
                it().updates_the(r.entity_id_2_domain_event_id_table)
                it().saves_the(r.transaction)

        # Process domain events in background
        with the(r.process_domain_events_loop).calls(r.process_domain_events_action):
            it().processes_and_accepts_the(r.domain_events)
            it().notifies(r.transaction_id).with_the(r.plot_id)


markdown_node_1 = sunya.add_markdown_node(scenario, "A user adds a plot to a project - Overview")

markdown_node_1.markdown = """
A user adds a plot to a project. The system creates a polygon, validates and creates a plot questionnaire, and then creates the plot using domain events. Domain events are inserted into the database and processed asynchronously in the background.

This scenario uses domain events to ensure transactional consistency and enable asynchronous processing. The flow is divided into three phases: setup and orchestration, plot creation, and event persistence and processing.

### Steps

#### It sets up the domain event manager

The frontend calls the create plot API view with a transaction ID.</br>
**Note [1]**: The transaction_id is later used to call back to the frontend (using a server event) to inform about the status of the plot creation.</br>

The API view gets the domain event manager from thread storage.</br>
**Note [2]**: Every thread has its own instance of the domain_event_manager. The domain_event_manager is created if it does not yet exist for the current thread. The domain_event_manager is used as a Python context manager (using the 'with' statement). When we enter the domain_event_manager context, we increase its reference count. When the reference count goes to zero, we finalize the transaction and remove the domain_event_manager instance from the thread storage. Note that there is no database transaction that is associated with the domain event manager.</br>

The API view enters the domain event manager as a context to create a transaction.</br>
**Note [3]**: The life-cycle events for the transaction are: 1) It implicitly exists via the domain events in memory, 2) If we abort early then the transaction is rolled back and removed from memory, 3) It is saved to the database as domain events in the pending state, 4) The process_domain_events_action may abort and move the domain events to the rejected state, 5) The process_domain_events_action may accept and move the domain events to the accepted state.</br>

#### It creates the plot

See diagram 2 below for details of plot creation and creation of domain events.</br>

#### It saves and processes domain events

The API view sets the transaction payload to the plot ID.</br>
**Note [10]**: When observers of the transaction_id receive a callback, they will receive the id of the created plot.</br>

See diagram 3 below for details of domain event insertion and processing.</br>

### Diagram 1: Domain Event Manager Setup and Orchestration

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant CreatePlotApiView as CreatePlotApiView
    participant GetDomainEventManager as GetDomainEventManager (rule)
    participant DomainEventManager as DomainEventManager

    Note over Frontend,CreatePlotApiView: Create Plot
    User->>Frontend: create plot
    Frontend->>CreatePlotApiView: calls(transaction_id)
    Note over CreatePlotApiView: See [1]

    CreatePlotApiView->>GetDomainEventManager: get_domain_event_manager()
    Note over GetDomainEventManager: See [2]
    GetDomainEventManager-->>CreatePlotApiView: domain_event_manager

    CreatePlotApiView->>DomainEventManager: enter as context
    DomainEventManager->>DomainEventManager: increase reference count
    DomainEventManager->>DomainEventManager: store event_sequence_number
    Note over DomainEventManager: See [3]

    Note over CreatePlotApiView: Create the plot
    Note over CreatePlotApiView: See diagram 2 below for details

    Note over CreatePlotApiView: Finish CreatePlotApiView
    Note over CreatePlotApiView: See [10]
    CreatePlotApiView->>DomainEventManager: set transaction_payload to plot_id

    Note over CreatePlotApiView: See diagram 3 below for details
```
"""


markdown_node_2 = sunya.add_markdown_node(scenario, "A user adds a plot to a project - Plot Creation")

markdown_node_2.markdown = """
This diagram shows the detailed plot creation process including polygon creation, questionnaire validation, domain event creation, and adding the plot to the project.

### Steps

#### It creates value objects

**Note [4]**: The creation of polygons and plot_questionnaires is not based on domain events since they are just values.</br>

The API view calls `CreatePolygon` to create the polygon.</br>
The polygon is created and a rollback action is added to the domain event manager to delete the polygon if the transaction fails.</br>

The API view calls `CreatePlotQuestionnaire` to validate and create the plot questionnaire.</br>
The questionnaire values are validated against the plot questionnaire schema.</br>
The questionnaire is created and a rollback action is added to delete it if the transaction fails.</br>

#### It creates domain events for the plot

**Note [5]**: Clients can ask the domain event manager to append new domain events. The transaction_id is automatically assigned to these new domain events. The new domain events are stored in memory, and are inserted into the domain event table at the end of the transaction. When any client (of the domain event manager) reconstructs an entity by replaying domain events, they will ask the domain event manager for the events. They will receive all domain events up to the event_sequence_number (this is public data), plus the new domain events that were created in the same transaction (this data is private to the thread/transaction).</br>

The API view calls `CreatePlot` with the create_plot_form.</br>

**Note [6]**: When an action handles a call, it usually starts by reconstructing the entity from its domain events. The reconstruction is done from both the public events (up to the event_sequence_number in the transaction) and the private events in the current transaction. The action then verifies that the call is valid. E.g. if the call says "rename plot from old-name to new-name", but the current name of the plot is not "old-name" (someone else changed it in the meantime), then the action raises an exception that aborts the transaction. When the call is valid then the action calls the domain_event_manager to insert new domain events.</br>

**Note [7]**: When the client calls the create_domain_event action to create a new domain event it includes the list of entity ids of the affected entities. The domain events and associated entity ids are stored in the domain_event_manager. The create_domain_event raises an exception if there is no current transaction in the domain event manager.</br>

The action creates domain events for plot fields, plot owner, and plot questionnaire.</br>
The action reconstructs the plot from the domain events.</br>

**Note [8]**: Note that the plot may have errors. However, these errors are always determined dynamically when the plot is used. Therefore, we don't try to validate the plot at this point, but instead let the user deal with plot errors in the frontend later when the plot is already created.</br>

#### It adds the plot to the project

The `CreatePlot` action calls `AddPlotToProject` with the plot and project.</br>
The action reconstructs the plot from events to ensure consistency.</br>

**Note [9]**: The api request may contain a plot-list name that should be used instead of the default one. Below we find the correct plot list, which is either the default one or the one specified in the api request.</br>

The action finds the target plot list for the project.</br>
The action creates an add_plot_to_plot_list domain event.</br>
The action returns the plot_id.</br>

### Diagram 2: Plot Creation Details

```mermaid
sequenceDiagram
    participant CreatePlotApiView as CreatePlotApiView
    participant CreatePolygon as CreatePolygon (action)
    participant CreatePlotQuestionnaire as CreatePlotQuestionnaire (action)
    participant CreatePlot as CreatePlot (action)
    participant AddPlotToProject as AddPlotToProject (action)
    participant DomainEventManager as DomainEventManager

    Note over CreatePlotApiView,DomainEventManager: Create Plot

    Note over CreatePlotApiView: See [4]
    CreatePlotApiView->>CreatePolygon: create_polygon(polygon_data)
    CreatePolygon->>CreatePolygon: create polygon
    CreatePolygon->>DomainEventManager: add rollback_action to delete polygon

    CreatePlotApiView->>CreatePlotQuestionnaire: create_plot_questionnaire(questionnaire_data)
    CreatePlotQuestionnaire->>CreatePlotQuestionnaire: validate and create plot questionnaire
    CreatePlotQuestionnaire->>DomainEventManager: add rollback_action to delete plot_questionnaire

    CreatePlotApiView->>CreatePlot: create_plot(create_plot_form)
    Note over CreatePlot: See [5, 6, 7, 8]
    CreatePlot->>DomainEventManager: create update_plot_fields domain event
    CreatePlot->>DomainEventManager: create update_plot_owner domain event
    CreatePlot->>DomainEventManager: create update_plot_questionnaire domain event

    CreatePlot->>AddPlotToProject: add_plot_to_project(plot, project)
    AddPlotToProject->>AddPlotToProject: reconstruct plot from events
    AddPlotToProject->>AddPlotToProject: find plot_list for project
    Note over AddPlotToProject: See [9]
    AddPlotToProject->>DomainEventManager: create add_plot_to_plot_list domain event
    AddPlotToProject-->>CreatePlot: return

    CreatePlot-->>CreatePlotApiView: return plot_id
```
"""


markdown_node_3 = sunya.add_markdown_node(scenario, "A user adds a plot to a project - Event Persistence and Processing")

markdown_node_3.markdown = """
This diagram shows how domain events are persisted to the database and processed asynchronously in the background.

### Steps

#### It inserts domain events to the database

**Note [11]**: The insert_domain_events_action is called when the scope of the domain event manager context ends.</br>

The domain event manager calls `InsertDomainEvents`.</br>
The action locks the domain event table semaphore to ensure consistency.</br>
The action saves all domain events to the database in pending state.</br>
The action updates the entity_id to domain_event_id mapping table.</br>
The action saves the transaction metadata.</br>

**Note [12]**: The process_domain_events_action will load the domain events with the given transaction_id.</br>

#### It processes domain events in the background

**Note [13]**: The process_domain_events_loop is triggered at most twice per second. It runs in a single thread (there are no concurrent executions). It will find the next pending transaction_id in the domain_events table and call the process_domain_events_action to process these domain events. It will mark the domain events as accepted and call back to the observers of the transaction_id (such as the frontend).</br>

The process domain events loop finds the next pending transaction.</br>
The loop calls `ProcessDomainEvents` to validate and process the domain events.</br>
The action reconstructs affected entities by replaying events.</br>
The action marks the domain events as accepted or rejected.</br>
If accepted, the action updates view tables and saves the reconstructed entities.</br>
The loop notifies the frontend (and other observers) with the transaction_id and plot_id.</br>

### Diagram 3: Domain Event Insertion and Background Processing

```mermaid
sequenceDiagram
    participant Frontend as Frontend
    participant DomainEventManager as DomainEventManager
    participant InsertDomainEvents as InsertDomainEvents (action)
    participant ProcessDomainEventsLoop as ProcessDomainEventsLoop
    participant ProcessDomainEvents as ProcessDomainEvents (action)

    Note over DomainEventManager,ProcessDomainEvents: Process Domain Events

    Note over DomainEventManager: See [11]
    DomainEventManager->>InsertDomainEvents: insert_domain_events()
    InsertDomainEvents->>InsertDomainEvents: lock domain_event_table_semaphore
    InsertDomainEvents->>InsertDomainEvents: save domain_events
    InsertDomainEvents->>InsertDomainEvents: update entity_id_2_domain_event_id_table
    Note over InsertDomainEvents: See [12]

    Note over ProcessDomainEventsLoop: Background Processing
    Note over ProcessDomainEventsLoop: See [13]
    ProcessDomainEventsLoop->>ProcessDomainEventsLoop: find next pending transaction
    ProcessDomainEventsLoop->>ProcessDomainEvents: process_domain_events(transaction_id)
    ProcessDomainEvents->>ProcessDomainEvents: reconstruct entities by replaying events
    ProcessDomainEvents->>ProcessDomainEvents: mark domain events as accepted or rejected
    ProcessDomainEvents->>ProcessDomainEvents: update view tables and save entities (if accepted)
    ProcessDomainEventsLoop->>Frontend: notify(transaction_id, plot_id)
```
"""
