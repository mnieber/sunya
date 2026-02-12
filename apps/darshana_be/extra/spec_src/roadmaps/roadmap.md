# Goal of Darshana

The goal of the Darshana application is to allow the user to upload and view spec files that they have generated with the Sunya command-line tool.

## Glossary

Actor: an entity that participates in a scenario. Within a scenario, actors are referred to by their actor-key.
Actor-delta: a dictionary that shows how the fields of an actor have changed after performing a particular step.
Actor-key: a string that identifies an actor
Module spec(ification): a yaml file that describes a frontend or backend module within the component. For the purpose of this roadmap, we assume that the user has already prepared their module specs.
Component: the software component that is described by a set of spec files.
Scenario: a yaml file that describes a frontend or backend workflow within a component. For the purpose of this roadmap, we assume that the user already has already prepared their scenarios.
(Scenario) Step: a tuple that represents a step in the scenario. This tuple basically stores a sentence in which some of the terms are actor-keys that refer to actors (or role-keys that refer to roles).
Spec(ification): the combination of a set of module specs and scenarios that together describe the application that the user is interested in developing.

# TODO

A sunya config should have a component_name field.

## Milestones

### MS1: The user creates a local darshana server

1. When darshana is installed in the virtual env, then the user can start a local darshana server using `darshana <sunya.config.yaml>`.
2. This parses all spec files found from the `sunya.config.yaml` file and stores the results in memory
3. It also opens a browser window at the darshana home-page
4. The home-page shows links to different datasets:
   1. all components
   2. all actors

### MS2: The user browses the components

1. On the homepage the user clicks "all components" This opens the components page.
2. On the components page the user clicks on a component. This opens the component page.
3. On the component page the user sees a list of scenarios
4. The user clicks on a scenario to view it
   1. This opens the scenario page
5. The scenario page shows:
   1. the scenario markdown document
   2. the list of all actors that participate in the scenario
      1. the user can click on an actor (similar to how the user browses the actors in MS2)

### MS3: The user browses the actors

1. On the homepage the user clicks "all actors" This opens the actors page.
2. On the actors page the user clicks on a actor. This opens the actor page.
3. On the actor page the user sees:
   1. a list of scenarios (grouped by component) in which the actor participates.
   2. a list of steps that include this actor (grouped by goal, then scenario, then component)
      1. if a goal includes an actor, but the steps in that goal do not include the actor, then
         this goal is still shown in the list
      2. since the results are grouped by scenario, when the user clicks on any row within that scenario group, it opens the corresponding scenario page
      3. if the user clicks on the row that contains the component, then it opens the corresponding component page.
