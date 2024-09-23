import landler.backend.namespace as B
import landler.frontend.namespace as F
from sunya import FileWriter
from sunya.entrypoint import (
    get_module_and_scenario_names,
    write_modules,
    write_scenarios,
    parse_args,
)

config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="landler.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_module_names=[
        "backend/calculations",
        "backend/domain_events",
        "backend/facts",
        "backend/organizations",
        "backend/plot_analyses",
        "backend/plot_lists",
        "backend/plot_questionnaires",
        "backend/plots",
        "backend/polygons",
        "backend/project_analyses",
        "backend/project_analysis_jobs",
        "backend/projects",
        "backend/users",
        "frontend/checklist",
        "frontend/frames",
        "frontend/organizations",
        "frontend/maps",
        "frontend/users",
        "frontend/user_settings",
    ],
    all_scenario_names=[
        "backend/mrd1_a_user_signs_up_and_sees_a_checklist",
        "backend/mrd2_a_user_joins_the_demo_org_and_creates_an_org",
        "backend/mrd4_a_user_creates_a_project",
        "backend/mrd5_a_user_adds_a_plot_to_a_project",
        "backend/mrd6_a_staff_user_schedules_a_project_analysis",
        "frontend/ms2_a_user_interacts_with_the_checklist",
    ],
    module_by_name={
        "backend/calculations": B.Calculations,
        "backend/domain_events": B.DomainEvents,
        "backend/facts": B.Facts,
        "backend/organizations": B.Organizations,
        "backend/plot_analyses": B.PlotAnalyses,
        "backend/plot_lists": B.PlotLists,
        "backend/plot_questionnaires": B.PlotQuestionnaires,
        "backend/plots": B.Plots,
        "backend/polygons": B.Polygons,
        "backend/project_analyses": B.ProjectAnalyses,
        "backend/project_analysis_jobs": B.ProjectAnalysisJobs,
        "backend/projects": B.Projects,
        "backend/users": B.Users,
        "frontend/checklist": F.Checklist,
        "frontend/frames": F.Frames,
        "frontend/organizations": F.Organizations,
        "frontend/maps": F.Maps,
        "frontend/users": F.Users,
        "frontend/user_settings": F.UserSettings,
    },
)


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(config, args)

    file_writer = FileWriter("landler/spec")
    write_modules(config, module_names, file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
