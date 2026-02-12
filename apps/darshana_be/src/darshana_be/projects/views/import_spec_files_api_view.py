from darshana_be.common.form_serializer import FormSerializer
from darshana_be.common.permissions import user_is_authenticated
from darshana_be.common.serializers import EmptySerializer
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from darshana_be.projects.actions.import_spec_files import (
    UnknownSpecFileTypeError,
)
from darshana_be.projects.shortcuts import get_project_or_400
from darshana_be.api.utils.extend_schema import extend_schema
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser


class ImportSpecFilesSerializer(FormSerializer):
    sunya_config_fn = serializers.StringField(required=True)


class ImportSpecFilesApiView(APIView):
    parser_classes = (MultiPartParser,)

    @extend_schema(
        request=ImportSpecFilesSerializer,
        responses={
            200: EmptySerializer,
        },
        data=dict(
            project=get_project_or_400,
        ),
        permissions=[
            (status.HTTP_401_UNAUTHORIZED, user_is_authenticated),
        ],
    )
    def post(self, request, request_data, project):
        try:
            # TODO: convert this into a command line entrypoint
            # TODO: import the sunya_config_fn file so that all actors and relations
            # existing in memory
            # TODO: write actors and relations to the database
            # project = create_project(request_data.create_project_form)

            return Response(EmptySerializer().data, status=status.HTTP_200_OK)
        except UnknownSpecFileTypeError as e:
            raise ValidationError(code="UNKNOWN_SPEC_FILE_TYPE", detail=str(e))
