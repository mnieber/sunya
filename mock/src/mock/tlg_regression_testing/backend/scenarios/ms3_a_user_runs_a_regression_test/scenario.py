from sunya import G as g
from sunya import R as r
from sunya import add_scenario, get_scenario, goal, the

scenario_name = f"backend/ms3_a_user_runs_a_regression_test"


def start():
    with add_scenario(scenario_name):
        with goal("create a regression", r.test_result, "for the", g.geomodel):
            with the(r.user).initiates_regression_testing():
                with (
                    the(g.download_examples_action)
                    .downloads_the(g.example_repository)
                    .from_s3()
                ):
                    pass

                with the(g.run_regression_tests_action).runs_tests():
                    assert r.test_result

                with (
                    the(g.generate_html_report_action)
                    .generates_a(r.test_report)
                    .for_the(r.test_result)
                ):
                    with (
                        the(r.test_report)
                        .html_contains_collapsible_sections_with_the(r.output_diff)
                        .for_the_failing(r.examples)
                    ):
                        pass

        with goal("invalidate regression test examples"):
            with the(r.user).requests_to_invalidate_examples():
                with the(g.clear_examples_action).clears_the_s3_bucket_and_its(
                    g.example_repository
                ):
                    pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
