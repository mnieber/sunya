from atlases.views.create_atlas_api_view import CreateAtlasApiView
from atlases.views.get_atlas_briefs_api_view import GetAtlasBriefsApiView
from django.urls import path
from atlases.views.get_atlas_briefs_api_view import GetAtlasBriefsApiView
from atlases.views.delete_atlases_api_view import DeleteAtlasesApiView
from atlases.views.update_atlas_api_view import UpdateAtlasApiView

urlpatterns = [
    path(
        "create/",
        CreateAtlasApiView.as_view(),
        name="create-atlas",
    ),
    path(
        "list/",
        GetAtlasBriefsApiView.as_view(),
        #
        name="get-atlases",
    ),
    path(
        "atlases/<str:atlas_key>/update/",
        UpdateAtlasApiView.as_view(),
        name="update-atlas",
    ),
    path(
        "atlases/delete/",
        DeleteAtlasesApiView.as_view(),
        name="delete-atlases",
    ),
    path(
        "atlases/list/",
        GetAtlasBriefsApiView.as_view(),
        name="get-atlas-briefs",
    ),
]
