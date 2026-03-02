# Sunya roadmap

# TODO:

- steps can no longer be nested -> fix
- it's unclear how args and kwargs can be used in a Rel

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

## MS2: a scenario can dynamically declare modules in the component namespace (`c`)

1. The component namespace `c` is an object that stores dynamically created module specs
   1. An entry in `c` always follows the pattern of `<component_name>.<module_name>.<section_name>.<actor_name>`.
2. A scenario cannot assign to `m` but instead can declare that an actor exists in a certain module.
   1. E.g. by referencing `m.WebServer.Projects.Rules.GetFoo` the scenario can declare that...
      1. ...a WebServer component exists...
      1. ...a Projects module exists...
      1. ...with a Rules section...
      1. ...with a GetFoo (rule) actor.
3. The component namespace is global and shared between all scenarios.

## MS3: a scenario can create roles in the role namespace (`r`)

1. The role namespace `r` is an object that gives access to actors that are local to the scenario.
2. The expression `r.Foo` gets or creates a new role in `r` with `name=Foo` and `actor=None`.
   1. The actor can be set using `r.Foo.actor = <some_actor>`
   2. The actor cannot be changed again later.

## MS4: a scenario can declare relations between actors

1. A relation can be declared in the context of a...
   1. ...goal, e.g. `goal(the(r.user).opens_the(r.homepage))`
      1. This creates a goal-relation of ("the", r.user, "opens the", r.homepage)
