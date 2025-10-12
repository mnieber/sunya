from common.permissions import user_is_authenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from atlases.models import Atlas
from atlases.serializers import AtlasBriefSerializer
from api.utils.extend_schema import extend_schema
from common.utils.apply_filter_set_or_400 import apply_filter_set_or_400
from atlases.filters import AtlasFilterSet


class GetAtlasBriefsApiView(APIView):
    filterset_class = AtlasFilterSet
    queryset = Atlas.objects.none()

    @extend_schema(
        responses={
            200: AtlasBriefSerializer(many=True),
        },
        data=dict(),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def get(self, request):
        atlases = apply_filter_set_or_400(
            Atlas.objects.all(), AtlasFilterSet, request.query_params
        )
        serializer = AtlasBriefSerializer(atlases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
