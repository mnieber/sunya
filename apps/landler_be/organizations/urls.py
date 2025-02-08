from django.urls import path

from organizations.views.create_organization_api_view import CreateOrganizationApiView
from organizations.views.set_active_organization_api_view import (
    SetActiveOrganizationApiView,
)

urlpatterns = [
    path(
        "organizations/",
        CreateOrganizationApiView.as_view(),
        name="create-organization",
    ),
    path(
        "organizations/<uuid:organization_id>/set-active/",
        SetActiveOrganizationApiView.as_view(),
        name="set-active-organization",
    ),
]
