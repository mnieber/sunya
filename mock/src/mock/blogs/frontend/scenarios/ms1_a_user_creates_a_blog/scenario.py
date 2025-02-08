from sunya import (
    goal,
    add_scenario,
    get_scenario,
    the,
    G as g,
    R as r,
    I as i,
)


scenario_name = f"frontend/ms1_a_user_creates_a_blog"


def start():
    with add_scenario(scenario_name):
        with goal(i.create_a(r.blog).for_the(r.user)):
            with the(r.user).visits_the(g.blogs_route):
                pass

            with the(r.user).sees_the(g.blog_list_view):
                pass

            with the(r.user).presses_the(g.create_blog_button):
                pass

            with the(r.user).submits_the(g.blog_form_view):
                with the(g.frontend).calls_the(g.create_blog_mutation):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
