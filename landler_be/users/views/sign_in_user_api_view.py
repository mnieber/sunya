from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer
from users.actions.sign_in_user import (
    AccountIsNotActiveError,
    InvalidCredentialsError,
    sign_in_user,
)
from users.serializers import SignInUserFormSerializer


class SignInUserRequestSerializer(FormSerializer):
    sign_in_user_form = SignInUserFormSerializer()


class SignInUserApiView(APIView):
    @extend_schema(
        request=SignInUserRequestSerializer,
        responses={
            200: TokenObtainPairSerializer,
        },
        data=dict(),
        permissions=[],
    )
    def post(self, request, request_data):
        try:
            response_data = sign_in_user(request_data.sign_in_user_form)
        except InvalidCredentialsError:
            raise ValidationError({"non_field_errors": ["Invalid email or password."]})
        except AccountIsNotActiveError:
            raise ValidationError({"non_field_errors": ["Inactive acount."]})

        return Response(response_data, status=status.HTTP_200_OK)
