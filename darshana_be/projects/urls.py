from django.urls import path
from projects.views.delete_projects_api_view import DeleteProjectsApiView
from projects.views.create_project_api_view import CreateProjectApiView

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
]
