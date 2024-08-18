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
                with the(g.scenario_list_view).displays_the("scenarios"):
                    pass

            with the(e.user).clicks_on_a(e.scenario):
                register(e.project.scenarios[0], e.scenario)

                with (
                    the(g.step_tree_view)
                    .shows_the_root_steps_for_the_current(e.scenario)
                    .in_the(g.step_list_view)
                ):
                    pass

            with the(e.user).clicks_on_a_root_level_step():
                with the(g.step_list_view).highlights_the(e.step):
                    register(e.scenario.root_step.child_steps[0], e.step)

                with the(g.step_tree_view).opens_a_new(g.step_list_view).to_the_right():
                    pass

            with the(e.user).clicks_on_an_actor_link():
                with add_goal(
                    "view the selected", e.actor, "in the highlighted", e.step
                ):
                    with (
                        the("callback_for_the_highlight_facet")
                        .of_the(g.step_list_ctr)
                        .calls_the(g.set_highlighted_step_action)
                        .of_the(g.step_tree_state)
                    ):
                        with (
                            the(g.set_highlighted_step_action)
                            .updates_the(g.reconstructed_actor)
                            .of_the(g.step_tree_state)
                            .by_applying_each(g.field_delta_set)
                            .for_the_current(e.step)
                            .and_all_its_parent_steps()
                        ):
                            actor_(e)

                with the(g.actor_view).displays_the_highlighted(e.actor):
                    pass

            with the(e.user).clicks_on_actor_link_again():
                with the(g.step_view).redirects_to_the(g.actor_route):
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
