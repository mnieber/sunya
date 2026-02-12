from darshana_be.common.form_serializer import FormSerializer
from darshana_be.common.permissions import user_is_authenticated
from darshana_be.common.serializers import EmptySerializer
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from darshana_be.projects.actions.import_spec_files import (
    import_spec_files,
    ImportSpecFilesForm,
    UnknownSpecFileTypeError,
)
from darshana_be.projects.shortcuts import get_project_or_400
from darshana_be.api.utils.extend_schema import extend_schema
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser


class ImportSpecFilesSerializer(FormSerializer):
    files = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
        write_only=True,
    )


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
            import_spec_files(
                import_spec_files_form=ImportSpecFilesForm(files=request_data.files),
                project=project,
            )
            return Response(EmptySerializer().data, status=status.HTTP_200_OK)
        except UnknownSpecFileTypeError as e:
            raise ValidationError(code="UNKNOWN_SPEC_FILE_TYPE", detail=str(e))
