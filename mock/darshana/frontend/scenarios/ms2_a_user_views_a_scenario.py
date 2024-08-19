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

        with add_goal("view a", g.scenario, "in the current", g.project):
            with the(e.user).visits_the(g.project_route):
                with the(g.scenario_list_view).displays_the("scenarios"):
                    pass

            with the(e.user).clicks_on_the(e.scenario):
                register(e.project.scenarios[0], e.scenario)

                with (
                    the(g.step_tree_view)
                    .shows_the_root_steps_for_the(e.scenario)
                    .in_the(g.step_list_view)
                ):
                    pass

            with the(e.user).clicks_on_a_root_level_step():
                with the(g.step_list_view).highlights_the(e.step):
                    register(e.scenario.root_step.child_steps[0], e.step)

                with the(g.step_tree_view).opens_a_new(g.step_list_view).to_the_right():
                    pass

                with the(g.step_view).shows_the_expanded_highlighted(e.step):
                    pass

            with add_goal("view the selected", g.actor, "in the highlighted", g.step):
                with the(e.user).clicks_on_the_link_of_the(e.actor).in_the(g.step_view):
                    actor_(e)

                    with (
                        the("highlight facet")
                        .of_the(g.step_list_state)
                        .calls_the(g.set_highlighted_step_action)
                        .of_the(g.step_tree_state)
                    ):
                        with (
                            the(g.set_highlighted_step_action)
                            .updates_the(g.reconstructed_actor)
                            .of_the(g.step_tree_state)
                            .by_applying_each(g.field_delta_set)
                            .for_the(e.step)
                            .and_all_its_parent_steps()
                        ):
                            pass

                with the(g.actor_view).displays_the_highlighted(e.actor):
                    pass

            with the(e.user).clicks_again_on_the_link_of_the(e.actor):
                with the(g.step_view).redirects_to_the(g.actor_route).for_the(e.actor):
                    pass

    return get_scenario(scenario_name)


def actor_(e):
    register(
        F.Actors.Types.Actor(
            key="example:actor",
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
