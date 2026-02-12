from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from darshana_be.api.utils.extend_schema import extend_schema
from darshana_be.projects.actions.delete_projects import delete_projects, DeleteProjectsForm
from darshana_be.projects.serializers import DeleteProjectsFormSerializer
from darshana_be.common.permissions import user_is_authenticated


class DeleteProjectsApiView(APIView):
    @extend_schema(
        request=DeleteProjectsFormSerializer,
        responses={200: None},
        data=dict(),
        permissions=[
            (status.HTTP_401_UNAUTHORIZED, user_is_authenticated),
        ],
    )
    def post(self, request, request_data):
        delete_projects_form = DeleteProjectsForm(project_ids=request_data.project_ids)
        deleted_count = delete_projects(delete_projects_form)
        return Response({"deleted_count": deleted_count}, status=status.HTTP_200_OK)
