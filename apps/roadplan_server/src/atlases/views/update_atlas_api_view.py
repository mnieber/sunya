from common.permissions import user_is_authenticated
from atlases.actions.update_atlas import update_atlas
from atlases.serializers import AtlasSerializer, UpdateAtlasFormSerializer
from atlases.shortcuts import get_atlas_or_400
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer


class UpdateAtlasRequestSerializer(FormSerializer):
    update_atlas_form = UpdateAtlasFormSerializer()


class UpdateAtlasApiView(APIView):
    @extend_schema(
        request=UpdateAtlasRequestSerializer,
        responses={
            200: AtlasSerializer,
        },
        data=dict(atlas=get_atlas_or_400),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data, atlas):
        try:
            updated_atlas = update_atlas(
                update_atlas_form=request_data.update_atlas_form,
                atlas=atlas,
            )
        finally:
            pass

        return Response(AtlasSerializer(updated_atlas).data, status=status.HTTP_200_OK)
