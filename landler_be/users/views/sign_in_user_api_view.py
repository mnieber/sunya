from users.actions.sign_in_user import (
    sign_in_user,
    InvalidCredentialsError,
)
from users.serializers import SignInUserFormSerializer, UserSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer


class SignInUserRequestSerializer(FormSerializer):
    sign_in_user_form = SignInUserFormSerializer()


class SignInUserApiView(APIView):
    @extend_schema(
        request=SignInUserRequestSerializer,
        responses={
            200: UserSerializer,
        },
        data=dict(),
        permissions=[],
    )
    def post(self, request, request_data):
        try:
            user = sign_in_user(request_data.sign_in_user_form)
        except InvalidCredentialsError:
            raise ValidationError({"non_field_errors": ["Invalid email or password."]})

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
