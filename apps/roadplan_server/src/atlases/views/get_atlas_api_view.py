from common.permissions import user_is_authenticated
from atlases.shortcuts import get_atlas_or_400
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.utils.extend_schema import extend_schema
from atlases.models import Atlas
from atlases.serializers import AtlasSerializer


class GetAtlasApiView(APIView):
    queryset = Atlas.objects.none()

    @extend_schema(
        responses={
            200: AtlasSerializer(many=False),
        },
        data=dict(
            atlas=get_atlas_or_400,
        ),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def get(self, request, atlas):
        serializer = AtlasSerializer(atlas, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
