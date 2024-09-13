from django.urls import path
from projects.views.delete_projects_api_view import DeleteProjectsApiView
from projects.views.create_project_api_view import CreateProjectApiView
from projects.views.update_project_api_view import UpdateProjectApiView
from projects.views.import_spec_files_api_view import ImportSpecFilesApiView

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
]
