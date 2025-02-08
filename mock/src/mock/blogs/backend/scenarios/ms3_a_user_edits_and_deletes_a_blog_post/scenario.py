from sunya import (
    G as g,
    R as r,
    I as i,
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
)


scenario_name = f"backend/ms3_a_user_edits_and_deletes_a_blog_post"


def start():
    with add_scenario(scenario_name):
        with goal(i.edit_a(r.blog_post).in_the(r.blog)):
            with the(g.update_blog_post_api_view).calls_the(g.update_blog_post_action):
                with it().runs_the(g.has_forbidden_words_rule):
                    pass

        with goal(i.delete_some(r.blog_posts).in_the(r.blog)):
            with the(g.delete_blog_posts_api_view).calls_the(
                g.delete_blog_posts_action
            ):
                pass

    return get_scenario(scenario_name)


def run():
    from ..ms2_a_user_creates_a_blog_post import scenario as ms2_scenario

    run_scenario(ms2_scenario)

    assert r.user
    assert r.blog
    assert r.blog_post

    # Create a list of blog posts for the delete operation
    r.blog_posts = [r.blog_post]

    return start()


if __name__ == "__main__":
    run()
