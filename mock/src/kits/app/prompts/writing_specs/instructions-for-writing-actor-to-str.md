# Instructions for writing actor_to_str.py files

When writing an actor_to_str.py file, please follow the example in the blogs/backend/actor_to_str.py file.

## Purpose of actor_to_str

The purpose of the actor_to_str function is to generate a human-readable name for an entity, such that it identifies that entity.
Every entity that is declared in a module spec or entities.py file (or its baseclass) should have a corresponding actor_to_str
function in one of the actor_to_str.py files that are used in the mock code.

## Structure of the generated str

The generated str follows the structure of (name+)(sub-type):type. For example, in paused+job-list:list the
name is `paused`, the sub-type is job-list, and the type is list. This tells us that the entity is an instance with
name `paued` that is a list, and more specifically it's a job-list. Note that paused+job-:list is an equivalant name
that is more readable and therefore preferred. In other words, a hyphen may be used to indicate that the type (`list`)
is also a suffix of the sub-type.
