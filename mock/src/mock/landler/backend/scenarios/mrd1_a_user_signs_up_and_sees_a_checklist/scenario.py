from sunya import (
    goal,
    add_scenario,
    get_scenario,
    G as g,
    I as i,
    R as r,
    comment,
    it,
    the,
)

scenario_name = f"backend/mrd1_a_user_signs_up_and_sees_a_checklist"


def start():
    with add_scenario(scenario_name):

        # sign up
        with goal(i.sign_up_as_a(r.user)):
            with the(g.frontend).calls_the(g.sign_up_user_api_view):

                # create user
                with it().calls_the(g.create_user_action):
                    with it().creates_the(r.user):
                        assert r.user

                # activate account
                with it().calls_the(g.activate_user_account_action):
                    assert r.user.is_active

                # create checklist
                with goal(i.create_a(r.checklist).for_the(r.user)):
                    with it().calls_the(g.get_or_create_checklist_action):
                        with it().creates_the(r.checklist).for_the(r.user):
                            comment(
                                r.checklist,
                                is_a=g.Checklist(
                                    items=[
                                        "Welcome",
                                        "Join the demo organization",
                                        "Add your organization",
                                        "Create a project",
                                        "Add a plot",
                                        "Trigger a project-analysis",
                                    ]
                                ),
                            )

        # sign in
        with goal(i.sign_in_as_a(r.user)):
            with the(g.frontend).calls_the(g.sign_in_user_api_view):
                with it().calls_the(g.sign_in_user_action):
                    with it().sets_the_current_user_in_the(g.user_session).to(r.user):
                        assert g.user_session.user == r.user

                    with it().marks_the(r.user).as_authenticated():
                        assert r.user.is_authenticated

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
