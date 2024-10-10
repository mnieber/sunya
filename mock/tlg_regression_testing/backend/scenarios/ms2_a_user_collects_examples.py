from sunya import (
    add_goal,
    add_actor,
    add_scenario,
    get_scenario,
    get_scenario_name,
    add_role,
    the,
    G as g,
)
import tlg_regression_testing.backend.namespace as B

scenario_name = f"backend/{get_scenario_name(__file__)}"


def start():
    geomodel = add_role("Geomodel")
    selector = add_role("Selector")
    examples = add_role("Examples")
    s3_filename = add_role("S3Filename")
    example_repository_stat = add_role("ExampleRepositoryStat")

    with add_scenario(scenario_name):
        with add_goal("collect input/output", examples, "for the", geomodel):
            with the(geomodel).runs_with_input():
                with (
                    the(g.collect_regression_testing_examples_action)
                    .calls_the(g.download_example_repository_stat_action)
                    .to_download_the_current(example_repository_stat)
                ):
                    example_repository_stat.actor = example_repository_stat_()

                with (
                    the(g.collect_regression_testing_examples_action)
                    .uses_the(example_repository_stat)
                    .to_determine_which_selectors_need_additional_examples()
                ):
                    pass

                with the(
                    g.collect_regression_testing_examples_action
                ).runs_each_selected(
                    selector
                ).to_check_if_the_input_matches_the_selector_criteria():
                    with (
                        the(g.collect_regression_testing_examples_action)
                        .calls_(g.upload_example_action)
                        .to_upload_new_examples_to_s3()
                    ):
                        with (
                            the(g.upload_example_action)
                            .uses_a_dedicated(s3_filename)
                            .for_the_nth_example_to_prevent_writing_more_examples_than_needed()
                        ):
                            pass

    return get_scenario(scenario_name)


def example_repository_stat_():
    return add_actor(
        B.IO.Models.ExampleRepositoryStat(
            nr_of_stored_examples_by_selector_name={"cover_crop_last_year": 2}
        ),
        name="example_repository_stat",
    )


def run():
    return start()


if __name__ == "__main__":
    run()
