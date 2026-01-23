# Goal of Darshana

The goal of the Darshana application is to allow the user to upload and view spec files that they have generated with the Sunya command-line tool.

## Glossary

Actor: an entity that participates in a scenario. Within a scenario, actors are referred to by their actor-key.
Actor-delta: a dictionary that shows how the fields of an actor have changed after performing a particular step.
Actor-key: a string that identifies an actor
Module spec(ification): a yaml file that describes a frontend or backend module within the project. For the purpose of this roadmap, we assume that the user has already prepared their module specs.
Project: the software project that is described by a set of spec files.
Scenario: a yaml file that describes a frontend or backend workflow within a project. For the purpose of this roadmap, we assume that the user already has already prepared their scenarios.
(Scenario) Step: a tuple that represents a step in the scenario. This tuple basically stores a sentence in which some of the terms are actor-keys that refer to actors (or role-keys that refer to roles).
Spec(ification): the combination of a set of module specs and scenarios that together describe the application that the user is interested in developing.

## Milestones

### MS1: The user creates a project

1. The user visits the projects route and creates a new project
   1. They enter the project name
   2. The user presses the upload-files button to select their spec files
      1. They can select multiple spec files to be uploaded
      2. The user can delete some of their uploaded files
      3. When the user presses the upload button to confirm the selected files
         1. They are then redirected to the project route

### MS2: The user views a scenario

1. On the project route the user sees a list of scenarios
2. The user clicks on a scenario to view it
   1. This opens the step-tree-viewer
3. The step-tree-viewer shows the root-level steps in the scenario in a list-view
   1. When the user clicks on a root-level step, then this expands the step to show a list of child-steps.
   2. The actors within each step are shown as links
      1. When the user clicks the actor link then this actor is shown in the actor view below the step view
      2. When the user clicks the link icon (shown after the actor link) then they are redirected to the actor route for this actor
   3. The other terms in the step are shown as simple strings
4. Below the step-view there is an actor view that shows the currently highlighted actor
   1. The fields in the actor view are determined by aggregating all the actor-deltas from the root-step to the highlighted step
   2. The fields in the actor view that are changed in the current step are shown with a different color
