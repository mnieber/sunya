from sunya import get_actor_str, fact_to_string, NoValue, get_entity_delta


def get_scenario_description_context(scenario):
    context = dict(scenario_name=scenario.name, nodes=[])
    context["nodes"].append(_get_node_context(scenario.root_node))
    return context


def _get_node_context(node):
    result = dict()

    result[node.name] = fact_to_string(node.fact)

    if actors_created := _get_node_actors(node, add_created=True, add_updated=False):
        result["actors_created"] = actors_created

    if actors_updated := _get_node_actors(node, add_created=False, add_updated=True):
        result["actors_updated"] = actors_updated

    child_nodes = [_get_node_context(child_node) for child_node in node.nodes]
    if child_nodes:
        result["child_nodes"] = child_nodes

    return result


def _get_node_actors(node, add_created, add_updated):
    result = []
    for entity in node.entities:
        delta = get_entity_delta(node, entity)
        field_deltas = {}
        for field_name, (old_value_memo, new_value_memo) in delta.items():
            if add_created and old_value_memo is NoValue:
                field_deltas[field_name] = f"{new_value_memo} ({None})"
            elif (
                add_updated
                and old_value_memo is not NoValue
                and new_value_memo != old_value_memo
            ):
                field_deltas[field_name] = f"{new_value_memo} ({old_value_memo})"
        if field_deltas:
            result.append(
                dict(
                    name=get_actor_str(entity),
                    deltas=field_deltas,
                )
            )
    return result
