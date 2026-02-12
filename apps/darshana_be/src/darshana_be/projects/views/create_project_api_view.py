from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from darshana_be.api.utils.extend_schema import extend_schema
from darshana_be.projects.actions.create_project import (
    create_project,
    ProjectWithNameAlreadyExistsError,
)
from darshana_be.projects.serializers import CreateProjectFormSerializer, ProjectLeadSerializer
from darshana_be.common.permissions import user_is_authenticated
from darshana_be.common.form_serializer import FormSerializer


class CreateProjectRequestSerializer(FormSerializer):
    create_project_form = CreateProjectFormSerializer()


class CreateProjectApiView(APIView):
    @extend_schema(
        request=CreateProjectRequestSerializer,
        responses={201: ProjectLeadSerializer},
        data=dict(),
        permissions=[
            (status.HTTP_401_UNAUTHORIZED, user_is_authenticated),
        ],
    )
    def post(self, request, request_data):
        try:
            project = create_project(request_data.create_project_form)
        except ProjectWithNameAlreadyExistsError:
            raise ValidationError(code="PROJECT_WITH_NAME_ALREADY_EXISTS")

        return Response(
            ProjectLeadSerializer(project).data, status=status.HTTP_201_CREATED
        )
