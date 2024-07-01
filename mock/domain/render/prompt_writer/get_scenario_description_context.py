from sunya import actor_to_str, fact_to_string
from sunya.scenarios.store import NoValue, get_entity_delta


def get_scenario_description_context(scenario):
    context = dict(scenario=scenario, steps=[])
    for step in scenario.get_list_of_steps():
        context["steps"].append(
            dict(
                fact=step.fact,
                level=step.level,
                title=(step.level * "#") + " " + fact_to_string(step.fact) + "\n",
                actors_created=_get_step_actors(
                    step, add_created=True, add_updated=False
                ),
                actors_updated=_get_step_actors(
                    step, add_created=False, add_updated=True
                ),
            )
        )
    return context


def _get_step_actors(step, add_created, add_updated):
    result = []
    for entity in step.entities:
        delta = get_entity_delta(step, entity)
        field_deltas = []
        for field_name, (old_value, new_value) in delta.items():
            old_value_memo = _format(old_value)
            new_value_memo = _format(new_value)

            if add_created and old_value is NoValue:
                field_deltas.append((field_name, None, new_value_memo))
            elif (
                add_updated
                and old_value is not NoValue
                and new_value_memo != old_value_memo
            ):
                field_deltas.append((field_name, old_value_memo, new_value_memo))
        if field_deltas:
            result.append(
                dict(
                    name=actor_to_str(entity),
                    deltas=field_deltas,
                )
            )
    return result


def _format(x):
    try:
        return f"[{actor_to_str(x)}]"
    except Exception:
        return x
