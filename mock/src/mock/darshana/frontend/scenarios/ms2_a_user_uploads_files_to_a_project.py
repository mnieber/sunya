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
    spec_files = add_role("SpecFiles")
    user = add_role("User")
    project = add_role("Project")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")
        project.actor = add_actor(a_project, name="project")

        with add_goal("upload", spec_files, "to the", project):
            with the(g.user).visits_the(g.project_route):
                pass

            with the(g.user).presses_the(g.upload_spec_files_button):
                pass

            with the(g.user).selects_the(spec_files):
                pass

            with the(g.user).deletes_some_of_the(spec_files):
                pass

            with the(g.user).submits_the(g.upload_spec_files_form_view):
                with the(g.frontend).calls_the(g.upload_spec_files_mutation):
                    pass

    return get_scenario(scenario_name)


def run():
    from . import ms1_a_user_creates_a_project

    ms1_scenario = run_scenario(ms1_a_user_creates_a_project)
    user = ms1_scenario.get_entity_by_name("user")
    project = ms1_scenario.get_entity_by_name("project")

    return start(user, project)


if __name__ == "__main__":
    run()
