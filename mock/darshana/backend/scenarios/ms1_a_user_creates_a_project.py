import darshana.backend.namespace as B
from sunya import G as g
from sunya import add_actor, add_goal, add_role, add_scenario, get_scenario, the


def start():
    user = add_role("User")
    project = add_role("Project")
    spec_files = add_role("SpecFiles")
    scenario = add_role("Scenario")
    step = add_role("Step")
    actor = add_role("Actor")
    module_spec_files = add_role("ModuleSpecFiles")
    scenario_spec_files = add_role("ScenarioSpecFiles")

    scenario_name = "ms1-a-user-creates-a-project"
    with add_scenario(scenario_name):
        with add_goal("create a new", project, "for the", user):
            with the(g.create_project_api_view).calls_the(g.create_project_action):
                project_()

        with add_goal("upload", spec_files, "to the", project):
            with (
                the(g.upload_spec_files_api_view)
                .identifies_the(scenario_spec_files)
                .and_the(module_spec_files)
                .in_the(spec_files)
            ):
                pass

            with (
                the(g.upload_spec_files_api_view)
                .deletes_each(scenario)
                .from_the(project)
            ):
                pass

            with the(g.upload_spec_files_api_view).calls_the(
                g.import_spec_files_action
            ):
                with the(g.import_spec_files_action).deletes_all_data_in_the(project):
                    pass

                with (
                    the(g.import_spec_files_action)
                    .calls_the(g.import_scenario_spec_action)
                    .for_each_file_in_the(scenario_spec_files)
                ):
                    with the(
                        g.import_scenario_spec_action
                    ).iterates_the_tree_structure_of_the(scenario):
                        with the(g.import_scenario_spec_action).calls_the(
                            g.create_actor_action
                        ).for_each(actor):
                            pass

                        with the(g.import_scenario_spec_action).calls_the(
                            g.create_step_action
                        ).with_these(actor).instances():
                            pass

                        with the(g.import_scenario_spec_action).calls_the(
                            g.create_scenario_action
                        ).with_these(step).instances():
                            pass

                        _update_project()

    return get_scenario(scenario_name)


def project_():
    add_actor(
        B.Projects.Models.Project(
            name="My Darshana Project",
            description="A project to test Darshana",
        ),
        name="project",
        role="Project",
    )


def _update_project():
    g.project.scenarios = (
        [
            B.Scenarios.Models.Scenario(
                name="My First Scenario",
                project=g.project,
                root_step=B.Steps.Models.Step(
                    fact=_create_fact("root"),
                    child_steps=[
                        B.Steps.Models.Step(
                            fact=_create_fact(
                                "the", "alice@example.com:user", "creates a", "Project"
                            ),
                            child_steps=[
                                B.Steps.Models.Step(
                                    fact=_create_fact(
                                        "the",
                                        "alice@example.com:user",
                                        "uploads the",
                                        "SpecFiles",
                                    ),
                                )
                            ],
                        ),
                        B.Steps.Models.Step(
                            fact=_create_fact(
                                "the",
                                "alice@example.com:user",
                                "clicks on a",
                                "Scenario",
                            ),
                        ),
                    ],
                ),
            )
        ],
    )


def _create_fact(*fact_bit_strings):
    fact_bits = []
    for fact_bit_string in fact_bit_strings:
        type_name = (
            "role"
            if fact_bit_string[0] == fact_bit_string[0].upper()
            else "actor" if ":" in fact_bit_string else "string"
        )
        fact_bits.append(
            B.Steps.Models.FactBit(type_name=type_name, value=fact_bit_string)
        )
    return tuple(fact_bits)


def run():
    return start()


if __name__ == "__main__":
    run()
