# Instructions for writing backend scenario files

When writing the backend scenario file for a milestone in the roadmap, please follow the example in the blogs/backend/scenarios/ms1_a_user_creates_a_blog/scenario.py file.

## Scenarios can declare actors, goals and steps

An actor is declared using the `r` (roles) namespace, e.g. r.create_blog_form declares an actor that represents a form. Some actors are also participants in the sequence diagram (i.e. they have a vertical lane). You can do this using the `participant` function that declares a mock code unit in the `m` (modules) namespace and a related actor using the `role=r.some_actor` argument.
