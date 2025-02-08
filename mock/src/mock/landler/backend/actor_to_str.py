from sunya import actor_to_str
import mock.landler.backend.namespace as B
from sunya import get_now_suffix


@actor_to_str.method((B.Organizations.Models.Organization,))
def organization_to_str(organization):
    return f"{organization.name}+:organization"


@actor_to_str.method((B.Organizations.Models.OrganizationStaffSettings,))
def organization_staff_settings_to_str(organization_staff_settings):
    return (
        f"{organization_staff_settings.organization.name}+:organization-staff-settings"
    )


@actor_to_str.method((B.Organizations.Models.OrganizationMembership,))
def organization_membership_to_str(organization_membership):
    return (
        f"({organization_membership.organization.name})-"
        + f"({organization_membership.user.email})-"
        + f"({organization_membership.role})+:organization-membership"
    )


@actor_to_str.method((B.Calculations.Models.Calculation,))
def calculation_to_str(calculation):
    return f"{calculation.name}+:calculation"


@actor_to_str.method((B.DomainEvents.Models.DomainEvent,))
def domain_event_to_str(domain_event):
    return f"{domain_event.type_id}-{domain_event.timestamp}+:domain_event"


@actor_to_str.method((B.Facts.Models.Fact,))
def fact_to_str(fact):
    return f"{fact.name}+:fact"


@actor_to_str.method((B.PlotAnalyses.Models.PlotAnalysis,))
def plot_analysis_to_str(plot_analysis):
    return f"{plot_analysis.plot.name}@{plot_analysis.now}+:plot-analysis"


@actor_to_str.method((B.PlotLists.Models.PlotList,))
def plot_list_to_str(plot_list):
    return f"{plot_list.name}+:plotList"


@actor_to_str.method((B.Projects.Models.Project,))
def project_to_str(project):
    return f"{project.name}+:project{get_now_suffix(project)}"


@actor_to_str.method((B.Projects.Models.ProjectMembership,))
def project_membership_to_str(project_membership):
    return (
        f"({project_membership.project.name})-"
        + f"({project_membership.organization.name})-"
        + f"({project_membership.role})+:project-membership"
    )


@actor_to_str.method((B.PlotQuestionnaires.Models.PlotQuestionnaire,))
def plot_questionnaire_to_str(plot_questionnaire):
    return f"{plot_questionnaire.plot.name}+:plot-questionnaire"


@actor_to_str.method((B.Plots.Models.Plot,))
def plot_to_str(plot):
    return f"{plot.name}+:plot{get_now_suffix(plot)}"


@actor_to_str.method((B.Polygons.Models.Polygon,))
def polygon_to_str(polygon):
    return f"{polygon.crc}+:polygon"


@actor_to_str.method((B.ProjectAnalyses.Models.ProjectAnalysis,))
def project_analysis_to_str(project_analysis):
    return f"{project_analysis.project.name}+:project-analysis"


@actor_to_str.method((B.ProjectAnalysisJobs.Models.ProjectAnalysisJob,))
def project_analysis_job_to_str(project_analysis_job):
    return f"{project_analysis_job.project.name}+:project-analysis-job"


@actor_to_str.method((B.Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"


@actor_to_str.method((B.Checklists.Models.Checklist,))
def checklist_to_str(checklist):
    return f"{checklist.owner.email}+:checklist"


@actor_to_str.method((B.Checklists.Models.ChecklistItem,))
def checklist_item_to_str(checklist_item):
    return f"{checklist_item.name}+:checklist-item"
