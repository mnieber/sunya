import mock.landler.backend.namespace as B


def resolve_entity_in_global_namespace(name):
    # Users module
    if name == "sign_up_user_api_view":
        return B.Users.Api.SignUpUserApiView()
    if name == "create_user_action":
        return B.Users.Actions.CreateUser()
    if name == "activate_user_account_action":
        return B.Users.Actions.ActivateUserAccount()
    if name == "sign_in_user_api_view":
        return B.Users.Api.SignInUserApiView()
    if name == "sign_in_user_action":
        return B.Users.Actions.SignInUser()

    # Organizations
    if name == "create_organization_action":
        return B.Organizations.Actions.CreateOrganization()
    if name == "add_user_to_organization_action":
        return B.Organizations.Actions.AddUserToOrganization()
    if name == "set_active_organization_action":
        return B.Organizations.Actions.SetActiveOrganization()
    if name == "create_organization_api_view":
        return B.Organizations.Api.CreateOrganizationApiView()
    if name == "add_user_to_demo_organization_api_view":
        return B.Organizations.Api.AddUserToDemoOrganizationApiView()
    if name == "set_active_organization_api_view":
        return B.Organizations.Api.SetActiveOrganizationApiView()
    if name == "generate_random_display_name_rule":
        return B.Organizations.Rules.GenerateRandomDisplayName()

    # Projects
    if name == "create_project_api_view":
        return B.Projects.Api.CreateProjectApiView()
    if name == "create_project_action":
        return B.Projects.Actions.CreateProject()
    if name == "add_organization_to_project_action":
        return B.Projects.Actions.AddOrganizationToProject()

    # Plots
    if name == "create_plot_api_view":
        return B.Plots.Api.CreatePlotApiView()
    if name == "create_plot_action":
        return B.Plots.Actions.CreatePlot()
    if name == "add_plot_to_project_action":
        return B.Projects.Actions.AddPlotToProject()

    # Checklists module
    if name == "get_or_create_checklist_action":
        return B.Checklists.Actions.GetOrCreateChecklist()
    if name == "update_checklist_item_action":
        return B.Checklists.Actions.UpdateChecklistItem()

    # Project Analysis
    if name == "create_project_analysis_job_api_view":
        return B.ProjectAnalysisJobs.Api.CreateProjectAnalysisJob()
    if name == "create_project_analysis_job_action":
        return B.ProjectAnalysisJobs.Actions.CreateProjectAnalysisJob()
    if name == "create_project_analysis_action":
        return B.ProjectAnalyses.Actions.CreateProjectAnalysis()
    if name == "run_project_analysis_action":
        return B.ProjectAnalyses.Actions.RunProjectAnalysis()
    if name == "run_plot_analysis_action":
        return B.PlotAnalyses.Actions.RunPlotAnalysis()

    # Project Analysis Queue
    if name == "project_analysis_queue":
        return B.ProjectAnalysisJobs.Models.ProjectAnalysisQueue()

    # Backend entities
    if name == "user_session":
        return B.UserSession()

    return None
