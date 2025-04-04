# Instructions for writing resolve_entity_in_global_namespace.py files

When writing an resolve_entity_in_global_namespace.py file, please follow the example in the blogs/backend/resolve_entity_in_global_namespace.py file.

## Purpose of resolve_entity_in_global_namespace

The purpose of the resolve_entity_in_global_namespace function is to create a global resource entity that is mentioned in
a scenario. For every global resource (such as `g.user_session`) an entry should be added to the related `resolve_entity_in_global_namespace`
function. This entry should instantiate the corresponding entity from the mock code-units in the module specs, or from the entities in
the entities.py file. The entities that are instantiated are imported from the related namespace.py files.
