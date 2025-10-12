from atlases.actions.create_atlas import create_atlas
from atlases.serializers import AtlasSerializer, CreateAtlasFormSerializer
from common.permissions import user_is_authenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer


class CreateAtlasRequestSerializer(FormSerializer):
    create_atlas_form = CreateAtlasFormSerializer()


class CreateAtlasApiView(APIView):
    @extend_schema(
        request=CreateAtlasRequestSerializer,
        responses={
            200: AtlasSerializer,
        },
        data=dict(),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data):
        try:
            atlas = create_atlas(
                create_atlas_form=request_data.create_atlas_form,
                owner=request.user,
            )
        finally:
            pass

        return Response(AtlasSerializer(atlas).data, status=status.HTTP_201_CREATED)
