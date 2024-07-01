from organizations.actions.add_user_to_organization import (
    UserAlreadyInOrganizationError,
    add_user_to_organization,
)
from organizations.actions.create_organization import (
    CreateOrganizationForm,
    OrganizationWithNameAlreadyExistsError,
    create_organization,
)
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from common.extend_schema import extend_schema
from users.actions.create_user import UserWithEmailAlreadyExistsError, create_user
from users.serializers import CreateUserFormSerializer, UserSerializer


class SignUpUserRequestSerializer(serializers.Serializer):
    create_user_form = CreateUserFormSerializer()


class SignUpUserApiView(APIView):
    @extend_schema(
        request=SignUpUserRequestSerializer,
        responses={200: UserSerializer},
        data_spec=dict(),
        permissions=[],
    )
    def post(self, request, request_data):
        try:
            user = create_user(request_data.create_user_form)
            organization = create_organization(
                CreateOrganizationForm(name="My Organization"), owner=user
            )
            add_user_to_organization(user, organization)
        except UserWithEmailAlreadyExistsError:
            raise ValidationError(
                {"non_field_errors": [_("User with this email already exists")]}
            )
        except OrganizationWithNameAlreadyExistsError:
            raise ValidationError(
                {"non_field_errors": [_("Organization with this name already exists")]}
            )
        except UserAlreadyInOrganizationError:
            raise ValidationError(
                {"non_field_errors": [_("User is already in the organization")]}
            )

        return Response(UserSerializer(user).data)
