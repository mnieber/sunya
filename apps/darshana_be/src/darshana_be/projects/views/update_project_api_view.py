from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from darshana_be.api.utils.extend_schema import extend_schema
from darshana_be.projects.actions.update_project import (
    update_project,
    ProjectWithNameAlreadyExistsError,
)
from darshana_be.projects.serializers import UpdateProjectFormSerializer, ProjectLeadSerializer
from darshana_be.projects.shortcuts import get_project_or_400
from darshana_be.common.permissions import user_is_authenticated
from darshana_be.common.form_serializer import FormSerializer


class UpdateProjectRequestSerializer(FormSerializer):
    update_project_form = UpdateProjectFormSerializer()


class UpdateProjectApiView(APIView):
    @extend_schema(
        request=UpdateProjectRequestSerializer,
        responses={200: ProjectLeadSerializer},
        data=dict(
            project=get_project_or_400,
        ),
        permissions=[
            (status.HTTP_401_UNAUTHORIZED, user_is_authenticated),
        ],
    )
    def post(self, request, request_data, project):
        try:
            updated_project = update_project(request_data.update_project_form, project)
        except ProjectWithNameAlreadyExistsError:
            raise ValidationError(code="PROJECT_WITH_NAME_ALREADY_EXISTS")

        return Response(
            ProjectLeadSerializer(updated_project).data, status=status.HTTP_200_OK
        )
