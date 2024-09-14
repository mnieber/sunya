from common.permissions import user_is_authenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.serializers import ProjectLeadSerializer
from projects.shortcuts import get_project_or_400
from api.utils.extend_schema import extend_schema


class GetProjectApiView(APIView):
    @extend_schema(
        responses={
            200: ProjectLeadSerializer,
        },
        data=dict(
            project=get_project_or_400,
        ),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def get(self, request, project):
        return Response(ProjectLeadSerializer(project).data, status=status.HTTP_200_OK)
