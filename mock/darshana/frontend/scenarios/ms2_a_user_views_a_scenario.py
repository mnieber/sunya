from darshana.frontend.modules import Scenarios
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    register,
    the,
    G as g,
    get_entities,
)


def start(user, project):
    scenario_name = "ms2-a-user-views-a-scenario"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")
        register(project, name="project")

        with add_goal("view a", e.scenario, "in the", e.project):
            with the(e.user).visits_the(g.project_route):
                with the(g.frontend).displays_the(e.scenario_list):
                    scenario_list_(e)

            with the(e.user).clicks_on_a(e.scenario):
                with the(g.frontend).opens_the(g.step_tree_view):
                    step_tree_(e)

            with the(e.user).clicks_on_a_root_level_step():
                with the(g.frontend).highlights_the(e.step):
                    pass
                with the(g.frontend).opens_new_step_list_view():
                    pass

            with the(e.user).clicks_on_an_actor_link():
                with the(g.frontend).displays_actor_in(g.actor_view):
                    actor_(e)

            with the(e.user).clicks_on_actor_link_again():
                with the(g.frontend).redirects_to_the(g.actor_route):
                    pass

    return get_scenario(scenario_name)


def scenario_list_(e):
    register(
        Scenarios.Types.ScenarioList(
            scenarios=[
                Scenarios.Types.Scenario(name="Scenario 1"),
                Scenarios.Types.Scenario(name="Scenario 2"),
            ]
        ),
        e.scenario_list,
    )


def step_tree_(e):
    register(
        Scenarios.Types.StepTree(
            root_steps=[
                Scenarios.Types.Step(
                    description="Root Step 1",
                    child_steps=[Scenarios.Types.Step(description="Child Step 1")],
                ),
                Scenarios.Types.Step(description="Root Step 2"),
            ]
        ),
        e.step_tree,
    )


def actor_(e):
    register(
        Scenarios.Types.Actor(
            name="Example Actor",
            fields={
                "field1": "value1",
                "field2": "value2",
            },
            changed_fields=["field2"],
        ),
        e.actor,
    )


def run():
    from .ms1_a_user_creates_a_project import run as run_ms1

    ms1_scenario = run_ms1()
    user = ms1_scenario.get_entity_by_name("user")
    project = ms1_scenario.get_entity_by_name("project")

    return start(user, project)


if __name__ == "__main__":
    run()
