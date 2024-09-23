import darshana.frontend.modules as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    get_scenario_name,
    run_scenario,
    add_actor,
    add_role,
    the,
    G as g,
)


scenario_name = f"frontend/{get_scenario_name(__file__)}"


def start(a_user, a_project):
    actor = add_role("Actor")
    highlight_facet = add_role("HighlightFacet")
    parent_step = add_role("ParentStep")
    project = add_role("Project")
    reconstructed_actor_by_key = add_role("ReconstructedActorByKey")
    scenario = add_role("Scenario")
    scenarios = add_role("Scenarios")
    step = add_role("Step")
    user = add_role("User")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")
        project.actor = add_actor(a_project, name="project")

        with add_goal("view a", scenario, "in the", g.project):
            with the(g.user).visits_the(g.project_route):
                with (
                    the(g.project_page)
                    .calls_the(g.get_project_query)
                    .to_load_the(project)
                ):
                    pass

                with the(g.project_page).displays_the(scenarios).in_the(g.project):
                    pass

            with the(g.user).clicks_on_a(scenario):
                with the(g.user).is_redirected_to_the(g.scenario_route):
                    scenario.actor = scenario_()

                with (
                    the(g.step_tree_view)
                    .shows_the_root_steps_for_the(g.scenario)
                    .in_the(g.step_list_view)
                ):
                    pass

            with the(g.user).clicks_on_a_root_level(step):
                with the(g.step_list_view).highlights_the(step):
                    step.actor = step_()

            with the(g.user).expands_a_root_level(step):
                with the(g.step_tree_view).opens_a_new(
                    g.step_list_view
                ).below_the_expanded(step):
                    pass

            with add_goal(
                "view the selected",
                actor,
                "in the",
                g.step_tree_view,
            ):
                with the(g.user).clicks_on_the_link_of_an(actor):
                    actor.actor = actor_()

                    with (
                        the(highlight_facet)
                        .of_the(g.step_tree_state)
                        .calls_the(g.set_highlighted_actor_action)
                        .of_the(g.step_tree_state)
                    ):
                        with (
                            the(g.set_highlighted_actor_action)
                            .updates_the(reconstructed_actor_by_key)
                            .of_the(g.step_tree_state)
                            .by_applying_each(g.field_delta_set)
                            .for_each_actor_in_the_related(step)
                            .and_each(parent_step)
                        ):
                            pass

                with the(g.actor_view).displays_the_highlighted(actor):
                    pass

            with the(g.user).ctrl_clicks_on_the_link_of_the(g.actor):
                with the(g.step_tree_view).redirects_to_the(g.actor_route).for_the(
                    g.actor
                ):
                    pass

    return get_scenario(scenario_name)


def scenario_():
    return add_actor(g.project.scenarios[0], name="scenario")


def step_():
    return add_actor(g.scenario.root_step.child_steps[0], name="step")


def actor_():
    return add_actor(
        F.Actors.Types.Actor(
            key="example:actor",
            fields={
                "field1": "value1",
                "field2": "value2",
            },
            changed_fields=["field2"],
        ),
        name="actor",
    )


def run():
    from . import ms2_a_user_uploads_files_to_a_project

    ms2_scenario = run_scenario(ms2_a_user_uploads_files_to_a_project)
    user = ms2_scenario.get_entity_by_name("user")
    project = ms2_scenario.get_entity_by_name("project")

    return start(user, project)


if __name__ == "__main__":
    run()
