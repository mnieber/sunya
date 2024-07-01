import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.actions.block_token import block_token
from api.serializers import SignOutSerializer
from api.utils.parse_access_token_or_401 import parse_access_token_or_401
from api.utils.parse_refresh_token_or_401 import parse_refresh_token_or_401
from common.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class SignOutApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SignOutSerializer

    def post(self, request):
        serializer = SignOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access_token = parse_access_token_or_401(serializer.validated_data["access"])
        refresh_token = parse_refresh_token_or_401(serializer.validated_data["refresh"])

        refresh_token.blacklist()
        block_token(access_token["jti"])
        return Response(status=status.HTTP_205_RESET_CONTENT)
