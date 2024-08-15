from organizations.enums import UserInOrganizationRoles
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from common.form_serializer import FormSerializer
from organizations.actions.add_user_to_organization import (
    UserAlreadyInOrganizationError,
    add_user_to_organization,
)
from organizations.actions.create_organization import (
    CreateOrganizationForm,
    OrganizationWithNameAlreadyExistsError,
    create_organization,
)
from users.actions.create_user import (
    PasswordsDoNotMatchError,
    UserWithEmailAlreadyExistsError,
    create_user,
)
from users.serializers import CreateUserFormSerializer, UserSerializer


class SignUpUserRequestSerializer(FormSerializer):
    create_user_form = CreateUserFormSerializer()


class SignUpUserApiView(APIView):
    @extend_schema(
        request=SignUpUserRequestSerializer,
        responses={
            201: UserSerializer,
        },
        data=dict(),
        permissions=[],
    )
    def post(self, request, request_data):
        try:
            user = create_user(request_data.create_user_form)
            user.is_active = True
            user.save()
        except UserWithEmailAlreadyExistsError:
            raise ValidationError(code="USER_EMAIL_ALREADY_EXISTS")
        except PasswordsDoNotMatchError:
            raise ValidationError(code="PASSWORDS_DO_NOT_MATCH")

        try:
            organization = create_organization(
                CreateOrganizationForm(name="My Organization")
            )
            add_user_to_organization(organization, user, UserInOrganizationRoles.ADMIN)
        except OrganizationWithNameAlreadyExistsError:
            raise ValidationError(code="ORGANIZATION_NAME_ALREADY_EXISTS")
        except UserAlreadyInOrganizationError:
            raise ValidationError(code="USER_ALREADY_IN_ORGANIZATION")

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
