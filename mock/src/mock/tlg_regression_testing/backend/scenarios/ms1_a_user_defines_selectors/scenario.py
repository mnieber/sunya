from sunya import G as g
from sunya import R as r
from sunya import add_scenario, get_scenario, goal, the

scenario_name = f"backend/ms1_a_user_defines_selectors"


def start():
    with add_scenario(scenario_name):
        with goal("define regression-testing", r.selector_functions):
            with (
                the(r.user)
                .decorates_a(r.selector_function)
                .with_the(g.register_selector_action)
                .decorator()
            ):
                """
                They use the nr_of_example argument to control the number of examples
                that is collected.
                """
                assert r.selector_function.actor
            with (
                the(g.register_selector_action)
                .decorator_registers_the(r.selector_function)
                .with_the(g.selectors_repository)
            ):
                """
                The g.selectors_repository is a singleton
                """

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
