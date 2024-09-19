from sunya import get_actor_str, fact_to_string, NoValue, get_entity_delta
from sunya.entities import Entity
from sunya.scenarios.roles import Role


def get_scenario_description_context(scenario):
    context = dict(type="scenario", scenario_name=scenario.name, nodes=[])
    context["nodes"].append(_get_node_context(scenario.root_node))
    return context


def _get_node_context(node):
    result = dict()

    result[node.name] = fact_to_string(node.fact)

    if actors_introduced := _get_node_actors(node, add_created=True, add_updated=False):
        result["actors_introduced"] = actors_introduced

    if actors_updated := _get_node_actors(node, add_created=False, add_updated=True):
        result["actors_updated"] = actors_updated

    if pre_actor_key_by_role_name := _get_actor_key_by_role_name(
        node.pre_actor_key_by_role_name
    ):
        result["pre_actor_key_by_role_name"] = pre_actor_key_by_role_name

    if post_actor_key_by_role_name := _get_actor_key_by_role_name(
        node.post_actor_key_by_role_name, pre_actor_key_by_role_name
    ):
        result["post_actor_key_by_role_name"] = post_actor_key_by_role_name

    child_nodes = [_get_node_context(child_node) for child_node in node.nodes]
    if child_nodes:
        result["child_nodes"] = child_nodes

    return result


def _get_node_actors(node, add_created, add_updated):
    result = []
    for fact_bit in node.fact:
        if isinstance(fact_bit, Entity):
            entity = fact_bit
        elif isinstance(fact_bit, Role):
            entity = fact_bit.actor
        else:
            entity = None

        if not entity:
            continue

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


def _get_actor_key_by_role_name(
    actor_key_by_role_name, pre_actor_key_by_role_name=None
):
    return {
        role_name: actor_key[1]
        for role_name, actor_key in actor_key_by_role_name.items()
        if pre_actor_key_by_role_name is None
        or actor_key[1] != pre_actor_key_by_role_name.get(role_name)
    }
