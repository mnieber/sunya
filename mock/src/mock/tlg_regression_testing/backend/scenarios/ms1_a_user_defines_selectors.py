from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    get_scenario_name,
    add_actor,
    add_role,
    the,
    G as g,
)
import tlg_regression_testing.backend.namespace as B


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start():
    user = add_role("User")
    selector = add_role("Selector")

    with add_scenario(scenario_name):
        with add_goal("define regression-testing", selector, "functions"):
            with the(user).decorates_a(selector).with_the(
                g.register_selector_action
            ).decorator():
                selector.actor = selector_()
            with (
                the(g.register_selector_action)
                .decorator_registers_the(g.selector)
                .with_the(g.selectors_repository)
            ):
                with the(g.selectors_repository).is_a_singleton():
                    pass
                g.selectors_repository.selectors.append(selector.actor)

    return get_scenario(scenario_name)


def selector_():
    return add_actor(
        B.Selectors.Models.Selector(
            name="cover_crop_last_year",
            num_examples=5,
        ),
        name="selector",
    )


def run():
    return start()


if __name__ == "__main__":
    run()
