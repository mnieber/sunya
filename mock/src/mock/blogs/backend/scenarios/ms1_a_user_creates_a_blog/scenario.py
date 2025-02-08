from sunya import (
    the,
    goal,
    add_scenario,
    get_scenario,
    G as g,
    R as r,
    I as i,
    it,
)

scenario_name = f"backend/ms1_a_user_creates_a_blog"


def start():
    with add_scenario(scenario_name):
        with goal(i.create_a(r.blog).for_the(r.user)):
            with the(g.create_blog_api_view).calls_the(g.create_blog_action):
                with it().runs_the(g.has_forbidden_words_rule):
                    pass

                with it().creates_the(r.blog):
                    assert r.blog

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
