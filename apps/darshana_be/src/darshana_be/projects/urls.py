from django.urls import path
from darshana_be.projects.views.delete_projects_api_view import DeleteProjectsApiView
from darshana_be.projects.views.create_project_api_view import CreateProjectApiView
from darshana_be.projects.views.update_project_api_view import UpdateProjectApiView
from darshana_be.projects.views.import_spec_files_api_view import ImportSpecFilesApiView
from darshana_be.projects.views.get_project_api_view import GetProjectApiView
from darshana_be.projects.views.get_project_leads_api_view import GetProjectLeadsApiView

urlpatterns = [
    path(
        "create/",
        CreateProjectApiView.as_view(),
        name="create-project",
    ),
    path(
        "delete/",
        DeleteProjectsApiView.as_view(),
        name="delete-projects",
    ),
    path(
        "<str:project_key>/import-spec-files/",
        ImportSpecFilesApiView.as_view(),
        name="import-spec-files",
    ),
    path(
        "<str:project_key>/update/",
        UpdateProjectApiView.as_view(),
        name="update-project",
    ),
    path(
        "<str:project_key>/",
        GetProjectApiView.as_view(),
        name="get-project",
    ),
    path(
        "leads/list/",
        GetProjectLeadsApiView.as_view(),
        name="get-project-leads",
    ),
]
