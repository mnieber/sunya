from common.permissions import user_is_authenticated
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.utils.extend_schema import extend_schema
from atlases.actions.delete_atlases import delete_atlases
from atlases.serializers import DeleteAtlasesFormSerializer
from common.form_serializer import FormSerializer
from atlases.actions.delete_atlases import AtlasesNotFoundError


class DeleteAtlasesRequestSerializer(FormSerializer):
    delete_atlases_form = DeleteAtlasesFormSerializer()


class DeleteAtlasesApiView(APIView):
    @extend_schema(
        request=DeleteAtlasesRequestSerializer,
        responses={
            204: None,
        },
        data=dict(),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data):
        try:
            deleted_count = delete_atlases(request_data.delete_atlases_form)
        except AtlasesNotFoundError as e:
            return ValidationError(code="ATLASES_NOT_FOUND", detail=f"{e.missing_ids}")
        return Response(
            {"deleted_count": deleted_count}, status=status.HTTP_204_NO_CONTENT
        )
