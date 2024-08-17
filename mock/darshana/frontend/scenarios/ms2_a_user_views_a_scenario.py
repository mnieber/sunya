import darshana.frontend.modules as F
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
                with the(g.frontend).displays_the(g.scenario_list_view):
                    pass

            with the(e.user).clicks_on_a(e.scenario):
                register(e.project.scenarios[0], e.scenario)

                with the(g.frontend).shows_the(g.step_tree_view):
                    pass

            with the(e.user).clicks_on_a_root_level_step():
                with the(g.frontend).highlights_the(e.step):
                    register(e.scenario.root_step.child_steps[0], e.step)

                with the(g.frontend).opens_a_new(g.step_list_view):
                    pass

            with the(e.user).clicks_on_an_actor_link():
                with the(g.frontend).displays_actor_in(g.actor_view):
                    actor_(e)

            with the(e.user).clicks_on_actor_link_again():
                with the(g.frontend).redirects_to_the(g.actor_route):
                    pass

    return get_scenario(scenario_name)


def actor_(e):
    register(
        F.Actors.Types.Actor(
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
