from sunya import G as g
from sunya import R as r
from sunya import add_scenario, get_scenario, goal, the

scenario_name = f"backend/ms2_a_user_collects_examples"


def start():
    with add_scenario(scenario_name):
        with goal("collect", r.examples, "for the", g.geomodel):
            with (
                the(g.geomodel)
                .calls_the(g.geomodel_handle_function)
                .within_a(r.collect_example_context)
                .created_by_the(g.collect_example_function)
            ):
                with the(g.collect_example_function).creates_the_initial(
                    r.run_time_data
                ):
                    """
                    The run_time_data is stored in the thread local storage and can
                    be accessed by the geomodel.
                    """

                with the(g.geomodel_handle_function).runs_the(g.geomodel_code):
                    with the(g.geomodel_code).makes_an(r.api_request):
                        if running_in_replay_mode := g.true:
                            with (
                                the(g.geomodel_code)
                                .calls_the(g.regression_testing_cache)
                                .with_the(r.api_request_cache_key)
                                .to_obtain_the_cached(r.api_response)
                            ):
                                pass
                        else:
                            with (
                                the(g.geomodel_code)
                                .stores_the(r.api_response)
                                .in_the(r.runtime_data)
                            ):
                                """
                                If the geomodel is not running in replay mode, it stores the response in the
                                runtime data so that we can later (if we decide to collect the example) be
                                stored in the rtest example.
                                """

                with the(r.collect_example_context).exits():
                    with the(g.collect_example_function).decides_whether_to_collect_a(
                        r.rtest_example
                    ):
                        with the(g.collect_example_function).determines_whether_the(
                            g.geomodel
                        ).crashed():
                            """
                            We know the geomodel crashed if the runtime data has no output data.
                            """

                        """
                        Note that if the geomodel crashed then an rtest example is always collected.
                        Otherwise, it collects the example if this example is not already stored in the
                        example repository, and if some non-saturated selector function returns true.
                        """
                        assert r.collect_rtest_example is not None

                    if r.collect_rtest_example:
                        with (
                            the(g.collect_regression_testing_examples_action)
                            .calls_the(g.download_example_repository_stat_action)
                            .to_download_the_current(g.example_repository_stat)
                            .as_a_set_of(r.example_slot_files)
                        ):
                            pass

                        with (
                            the(g.collect_regression_testing_examples_action)
                            .uses_the(g.example_repository_stat)
                            .to_determine_which_selectors_need_additional_examples()
                        ):
                            pass

                        with (
                            the(g.collect_regression_testing_examples_action)
                            .runs_each_selected(r.selector)
                            .to_check_if_the_input_matches_the_selector_criteria()
                        ):
                            """
                            Each selector function returns a boolean value indicating
                            whether the input matches the selector criteria. If the selector returns
                            true and is not saturated, the example is collected.
                            """
                            with (
                                the(g.collect_regression_testing_examples_action)
                                .calls_the(g.upload_example_action)
                                .to_upload_new(r.rtest_examples)
                                .and_new(r.example_slot_files)
                                .to(g.s3)
                            ):
                                pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
