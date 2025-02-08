from sunya import (
    goal,
    add_scenario,
    get_scenario,
    run_scenario,
    the,
    G as g,
    R as r,
    I as i,
)


scenario_name = f"frontend/ms2_a_user_creates_a_blog_post"


def start():

    with add_scenario(scenario_name):
        with goal(i.create_a(r.blog_post).in_the(r.blog)):
            with the(r.user).visits_the(g.blogs_route):
                pass

            with the(r.user).clicks_on_a(r.blog).to_visit_the(g.blog_route):
                pass

            with the(r.user).presses_the(g.create_blog_post_button):
                pass

            with the(r.user).submits_the(g.blog_post_form_view):
                with the(g.frontend).calls_the(g.create_blog_post_mutation):
                    pass

    return get_scenario(scenario_name)


def run():
    from ..ms1_a_user_creates_a_blog import scenario as ms1_scenario

    run_scenario(ms1_scenario)

    assert r.user
    assert r.blog
    return start()


if __name__ == "__main__":
    run()
