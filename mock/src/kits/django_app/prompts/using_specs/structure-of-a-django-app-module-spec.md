# Structure of a backend module spec

The blogs/backend/modules/blogs.py file gives an example of a backend module spec.

## Purpose of a backend module spec

The purpose of the backend module spec is to give a high-level description of the backend code-units that are defined in a particular module. The module spec does not describe use-cases, as these are described in the scenarios.

## Top-level module class

The top-level data-structure is a so-called module class that inherits from Module. It acts as a namespace for all mock code-units for a specific module.

### Django models

The Models section of the module class describes the Django models that are based on the entities in the roadmap

### Actions

The Actions section describes the action functions. An action function is a function that changes the state (typically the database-state) of the application. You can think of the action functions as the "mutation-api" of the module. If the roadmap describes an operation that involves a state-change, then one of the backend module specs will probably describe an action function for it. Actions are not described directly in the module spec but they are declared implicitly in the scenario specs (e.g. by referring to Users.Actions.DeleteUser in the scenario spec).

### Api

The Api section describes the api views. ApiViews are not declared implicitly in the scenario specs.

### Enums

The Enums section describes the enums that are referenced in the Models section.

### Domain events

The DomainEvents section describes the domain events that would be interesting to send from the action functions.
The purpose of domain events is to inform external observers about what is going on in the system.
