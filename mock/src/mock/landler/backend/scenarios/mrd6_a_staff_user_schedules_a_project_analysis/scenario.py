from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
    G as g,
    R as r,
    I as i,
)


scenario_name = f"backend/mrd_6_a_staff_user_schedules_a_project_analysis"


def start():
    with add_scenario(scenario_name):

        # create a project analysis job
        with goal(i.create_a(r.project_analysis_job)):
            with the(g.frontend).calls_the(g.create_project_analysis_job_api_view):
                with it().calls_the(g.create_project_analysis_job_action):
                    with it().creates_a(r.project_analysis_job).and_adds_it_to_the(
                        g.project_analysis_queue
                    ):
                        assert r.project_analysis_job
                        assert (
                            r.project_analysis_job
                            in g.project_analysis_queue.project_analysis_jobs
                        )

        # find project analysis jobs to run
        with the(g.project_analysis_queue).finds_the(r.jobs_to_run):
            assert len(r.jobs_to_run)

        # run project analysis jobs
        for idx, a_project_analysis_job in enumerate(r.jobs_to_run):
            r.project_analysis_job = a_project_analysis_job
            r.project_analysis_job_loop_iteration = idx

            # run project analysis job
            with the(g.project_analysis_queue).runs_the(r.project_analysis_job):

                # create project analysis
                with goal(
                    i.create_a(r.project_analysis).from_a(r.project_analysis_job)
                ):
                    with the(g.project_analysis_queue).calls_the(
                        g.create_project_analysis_action
                    ):
                        with it().creates_a(r.project_analysis).and_adds_it_to_the(
                            r.project_analysis_job
                        ):
                            assert r.project_analysis.status == "RUNNING"

                        # determine project at now
                        with it().determines_the(
                            r.project_at_now
                        ).based_on_the_now_timestamp_of_the(r.project_analysis):
                            assert r.project_at_now._now_ == r.project_analysis.now

                        # determine plot list
                        with it().finds_the(r.default_plot_list).for_the(
                            r.project_at_now
                        ):
                            assert r.default_plot_list

                        # run plot analysis for each plot
                        with it().loops_over_all_plots_in_the(r.project_at_now):
                            for idx, a_plot in enumerate(r.default_plot_list.plots):
                                r.plot = a_plot
                                r.plot_loop_iteration = idx

                                # create a plot analysis
                                with goal(
                                    i.add_a(r.plot_analysis)
                                    .for_the(r.plot)
                                    .to_the(r.project_analysis)
                                ):
                                    with (
                                        it()
                                        .creates_a(r.plot_analysis)
                                        .for_the_current(r.plot)
                                        .and_adds_it_to_the(r.project_analysis)
                                    ):
                                        assert (
                                            r.plot_analysis.now
                                            == r.project_analysis.now
                                        )
                                        assert r.plot_analysis.status == "RUNNING"
                                        assert r.project_analysis.plot_analyses

                # run all plot analyses
                with goal(i.run_each(r.plot_analysis).in_the(r.project_analysis)):
                    with the(g.project_analysis_queue).calls_the(
                        g.run_project_analysis_action
                    ):
                        assert r.project_analysis.plot_analyses

                        for idx, a_plot_analysis in enumerate(
                            r.project_analysis.plot_analyses
                        ):
                            r.plot_analysis = a_plot_analysis
                            r.plot_analysis_loop_iteration = idx

                            # run plot analysis
                            with it().calls_the(g.run_plot_analysis_action):

                                # determine plot-at-now
                                with it().determines_the(
                                    r.plot_at_now
                                ).based_on_the_now_timestamp_of_the(r.plot_analysis):
                                    assert r.plot_at_now._now_ == r.plot_analysis.now

                                # create calcium plot analysis job
                                with it().creates_the(r.calcium_plot_analysis_job):
                                    assert (
                                        r.calcium_plot_analysis_job.polygon
                                        == r.plot_at_now.polygon
                                    )

            for idx, plot_analysis in enumerate(r.project_analysis.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(plot_analysis, idx)
                pass

    return get_scenario(scenario_name)


def run():
    from ..mrd5_a_user_adds_a_plot_to_a_project import scenario as mrd5_scenario

    run_scenario(mrd5_scenario)

    assert r.project

    return start()


if __name__ == "__main__":
    run()
