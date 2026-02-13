from sunya.scenarios.models.scenario import get_scenario


def note_over(level: int, note: any):
    assert level > 0, "Level must be greater than 0"

    scenario = get_scenario()
    first_actor_name = scenario.get_node().participants[level - 1]
    last_actor_name = scenario.get_node().participants[-1]
    return f"note over {first_actor_name}, {last_actor_name}: {note}"
