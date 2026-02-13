# Sunya roadmap

# TODO:

## Indentation

- Allow to use goal and end_goal to set indentation level, e.g. goal(2, it().foo())
  - And similar turn note -> into section (which have indentation level)
  - A goal will stretch the full width of the diagram, minus its indentation
  - end_goal will insert a <remove_line>
  - No need anymore to specify the start and end of a note-over

## Main relations

1. It would be cool if we can mark some steps as being a "main relation".
2. This allows us to create a structural diagram that shows a sub-set of actors and their main relations.
   1. E.g. :
      - Backend posts to Calcium
      - Calcium creates a Dag
      - Calcium calls the RunDagAction

## Create a small framework for magic namespaces

The current solution is very ad-hoc. Would be nice to have a principled solution.

# Completed milestones

## MS1: a scenario can declare actors in the global namespace (`g`)

1. The global namespace is an object in which the scenario can register any actor.
   1. It's accessed via the `g` symbol, e.g. `g.foo = 123`.
2. If you try to retrieve a non-existing actor from the global namespace then a KeyError is raised.
3. If you try to assign an already-existing actor then a KeyAlreadyExistsError is raised...
   1. ...unless if the same value is assigned.
4. When a actor is assigned to the global namespace then it becomes available to all scenarios.

## MS2: a scenario can dynamically declare modules in the module namespace (`m`)

1. The module namespace `m` is an object that stores dynamically created module specs
   1. An entry in `m` always follows the pattern of `<module_name>.<section_name>.<actor_name>`.
2. A scenario cannot assign to `m` but instead can declare that an actor exists in a certain module.
   1. E.g. by referencing `m.Projects.Rules.GetFoo` the scenario can declare that...
      1. ...a Projects module exists...
      2. ...with a Rules section...
      3. ...with a GetFoo (rule) actor.
3. The module namespace is global and shared between all scenarios.

## MS3: a scenario can create roles in the role namespace (`r`)

1. The role namespace `r` is an object that gives access to actors that are local to the scenario.
2. The expression `r.Foo` gets or creates a new role in `r` with `name=Foo` and `actor=None`.
   1. The actor can be set using `r.Foo.actor = <some_actor>`
   2. The actor cannot be changed again later.
3. A typical use-case is the participant function.
   1. This function is used as `participant(m.Projects.Rules.GetFoo, role=r.GetFoo)`
   2. The function returns a "participant GetFoo" string for the sequence diagram...
      1. ...and it sets `r.GetFoo.actor = m.Projects.Rules.GetFoo`

## MS4: a scenario can declare relations between actors

1. A relation can be declared in the context of a...
   1. ...goal, e.g. `goal(the(r.user).opens_the(r.homepage))`
      1. This creates a goal-relation of ("the", r.user, "opens the", r.homepage)
   1. ...action, e.g. `{r.ApiHandler >> r.Action}: a.calls(r.Form)`, or a
      1. This creates an action-relation of (r.ApiHandler, "calls", r.Action, "with", r.Form)
      2. Action-relations have a reference to their related goal

# Milestones

## MS: documentation for several libs can be organized in a single config file

1. Hierarchy is book -> lib -> module

## Claude can generate scenarios from a roadmap

1. We update the instructions for generating scenarios from a roadmap
2. We turn the scenario specs into separate markdown instructions for Claude
   1. These instructions include a lut from roles such as ActivateUserAccountAction to Users.Actions.ActivateUserAccount

## MS: user-supplied module specifications can be added to the module namespace

1. The scenario config can refer to module spec files that are supplied by the user.
2. These module spec files are automatically added to the module namespace...
   1. ...so that they can be used in scenarios.

## MS: A user inspects the markdown in dashana

1. Every step in the sequence diagram can...
   1. ...have an associated help-text and...
   2. ...embed a css class
2. This allow us to step through the help-texts and highlight the related row in the sequence diagram
