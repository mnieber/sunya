from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer
from common.permissions import user_is_authenticated
from common.serializers import EmptySerializer
from organizations.actions.add_user_to_demo_organization import (
    AddUserToDemoOrganizationForm,
    add_user_to_demo_organization,
)

User = get_user_model()


class AddUserToDemoOrganizationRequestSerializer(FormSerializer):
    add_user_to_demo_organization_form = AddUserToDemoOrganizationForm


class AddUserToDemoOrganizationApiView(APIView):
    @extend_schema(
        request=AddUserToDemoOrganizationRequestSerializer,
        responses={
            200: None,
        },
        data=dict(),
        permissions=[(status.HTTP_401_UNAUTHORIZED, user_is_authenticated)],
    )
    def post(self, request, request_data):
        user = request.user

        try:
            add_user_to_demo_organization(
                request_data.add_user_to_demo_organization_form
            )

            return Response(
                EmptySerializer().data,
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
