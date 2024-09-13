from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.serializers import ProjectSerializer
from projects.shortcuts import get_project_or_400
from api.utils.extend_schema import extend_schema


class GetProjectApiView(APIView):
    @extend_schema(
        responses={
            200: ProjectSerializer,
        },
        data=dict(
            project=get_project_or_400,
        ),
        permissions=[],
    )
    def get(self, request, project):
        return Response(
            ProjectSerializer(project).data,
            status=status.HTTP_200_OK
        )
