from sunya import (
    G as g,
    R as r,
    I as i,
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
)


scenario_name = f"backend/ms2_a_user_creates_a_blog_post"


def start():
    with add_scenario(scenario_name):
        with goal(i.create_a(r.blog_post).in_the(r.blog)):
            with the(g.create_blog_post_api_view).calls_the(g.create_blog_post_action):
                with the(g.create_blog_post_action).runs_the(
                    g.has_forbidden_words_rule
                ):
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
