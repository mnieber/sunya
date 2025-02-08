from sunya import goal, add_scenario, get_scenario, the, R as r, G as g, I as i

scenario_name = f"frontend/ms2_a_user_interacts_with_the_checklist"


def start():
    with add_scenario(scenario_name):
        with the(r.user).signs_in():
            pass

        with the(r.user).is_redirected_to_the(g.home_page_route):
            with goal(i.load_the(r.checklist)):
                with the(g.frontend).calls_the(g.get_checklist_query):
                    pass

        with the(r.user).views_the(r.checklist).on_the(g.home_page_route):
            pass

        with the(r.user).clicks_to_complete_the(r.first_item_to_complete):
            with the(g.frontend).calls_the(g.update_checklist_items_mutation):
                assert r.first_item_to_complete.is_completed

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
