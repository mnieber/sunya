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
    geomodel = add_role("Geomodel")
    selector = add_role("Selector")
    examples = add_role("Examples")
    test_report = add_role("Test_report")
    s3_filename = add_role("S3Filename")
    test_result = add_role("TestResult")
    output_diff = add_role("OutputDiff")
    example_repository = add_role("ExampleRepository")

    scenario_name = "tlg-geomodel-testing-workflow"
    with add_scenario(scenario_name):
        with add_goal("define regression-testing", selector, "functions"):
            with the(user).decorates_a(selector).with_the(
                g.register_selector
            ).decorator():
                selector.actor = selector_()
            with the(g.register_selector).decorator_registers_the(g.selector).with_the(
                g.selectors_repository
            ):
                g.selectors_repository.selectors.append(selector.actor)

        with add_goal("collect input/output", examples, "for the", geomodel):
            with the(geomodel).runs_with_input():
                with (
                    the(g.collect_regression_testing_examples_function)
                    .calls_the(g.io.download_examples_function)
                    .to_download_the_current(example_repository)
                ):
                    pass

                with (
                    the(g.collect_regression_testing_examples_function)
                    .uses_the(example_repository)
                    .to_determine_which_selectors_need_additional_examples()
                ):
                    pass

                with the(
                    g.collect_regression_testing_examples_function
                ).runs_each_selected(
                    selector
                ).to_check_if_the_input_matches_the_selector_criteria():
                    with (
                        the(g.collect_regression_testing_examples_function)
                        .calls_(g.io.upload_example_function)
                        .to_upload_new_examples_to_s3()
                    ):
                        with (
                            the(g.io.upload_example_function)
                            .uses_a_dedicated(s3_filename)
                            .for_the_nth_example_to_prevent_writing_more_examples_than_needed()
                        ):
                            pass

        with add_goal("create a regression", test_result, "for the", geomodel):
            with the(user).initiates_regression_testing():
                with the(
                    g.io.download_examples_function
                ).downloads_the_examples_from_s3():
                    pass
                with the(g.run_regression_tests_function).runs_tests():
                    test_result.actor = test_result_()
                with the(g.generate_html_report_function).generates_a(
                    test_report
                ).for_the(test_result):
                    with the(test_report).html_contains_collapsible_sections_with_the(
                        output_diff
                    ).for_the_failing(examples):
                        pass

        with add_goal("invalidate regression test examples"):
            with the(user).requests_to_invalidate_examples():
                with the(g.io.clear_examples_function).clears_the_s3_bucket_and_its(
                    example_repository
                ):
                    pass

    return get_scenario(scenario_name)


def selector_():
    return add_actor(
        B.Selectors.Models.Selector(
            name="cover_crop_last_year",
            num_examples=5,
        ),
        name="selector",
    )


def test_result_():
    return add_actor(
        B.Run.Models.TestResult(
            selector="cover_crop_last_year",
            input_id="test_1",
            passed=True,
        ),
        name="test_result",
    )


def run():
    return start()


if __name__ == "__main__":
    run()
