from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    get_scenario_name,
    add_role,
    the,
    G as g,
)


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start():
    geomodel = add_role("Geomodel")
    selector = add_role("Selector")
    examples = add_role("Examples")
    s3_filename = add_role("S3Filename")
    example_repository = add_role("ExampleRepository")

    with add_scenario(scenario_name):
        with add_goal("collect input/output", examples, "for the", geomodel):
            with the(geomodel).runs_with_input():
                with (
                    the(g.collect_regression_testing_examples_action)
                    .calls_the(g.download_examples_action)
                    .to_download_the_current(example_repository)
                ):
                    pass

                with (
                    the(g.collect_regression_testing_examples_action)
                    .uses_the(example_repository)
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


def run():
    return start()


if __name__ == "__main__":
    run()
