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
    examples = add_role("Examples")
    test_report = add_role("Test_report")
    test_result = add_role("TestResult")
    output_diff = add_role("OutputDiff")
    example_repository = add_role("ExampleRepository")

    with add_scenario(scenario_name):
        with add_goal("create a regression", test_result, "for the", geomodel):
            with the(user).initiates_regression_testing():
                with the(g.download_examples_action).downloads_the(
                    example_repository
                ).from_s3():
                    example_repository.actor = example_repository_()
                with the(g.run_regression_tests_action).runs_tests():
                    test_result.actor = test_result_()
                with the(g.generate_html_report_action).generates_a(
                    test_report
                ).for_the(test_result):
                    with the(test_report).html_contains_collapsible_sections_with_the(
                        output_diff
                    ).for_the_failing(examples):
                        pass

        with add_goal("invalidate regression test examples"):
            with the(user).requests_to_invalidate_examples():
                with the(g.clear_examples_action).clears_the_s3_bucket_and_its(
                    example_repository
                ):
                    pass

    return get_scenario(scenario_name)


def example_repository_():
    return add_actor(
        B.IO.Models.ExampleRepository(
            geomodel_name="geomodel_1",
            examples=[],
        ),
        name="example_repository",
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
