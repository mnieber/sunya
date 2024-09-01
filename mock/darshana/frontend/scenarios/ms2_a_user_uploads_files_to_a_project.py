from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    add_actor,
    add_role,
    the,
    G as g,
)


def start(user, project):
    spec_files = add_role("SpecFiles")

    scenario_name = "ms2-a-user-uploads-files-to-a-project"
    with add_scenario(scenario_name):
        add_actor(user, name="user", role="User")
        add_actor(project, name="project", role="Project")

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
    from .ms1_a_user_creates_a_project import run as run_ms1

    ms1_scenario = run_ms1()
    user = ms1_scenario.get_entity_by_name("user")
    project = ms1_scenario.get_entity_by_name("project")

    return start(user, project)


if __name__ == "__main__":
    run()
