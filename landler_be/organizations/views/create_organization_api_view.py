from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.extend_schema import extend_schema
from checklists.actions.update_checklist_item import update_checklist_item
from checklists.enums import ChecklistItemNames
from common.form_serializer import FormSerializer
from common.permissions import user_is_authenticated
from organizations.actions.add_user_to_organization import (
    UserAlreadyInOrganizationError,
    add_user_to_organization,
)
from organizations.actions.create_organization import (
    OrganizationWithNameAlreadyExistsError,
    create_organization,
)
from organizations.enums import UserInOrganizationRoles
from organizations.serializers import (
    CreateOrganizationFormSerializer,
    OrganizationSerializer,
)


class CreateOrganizationRequestSerializer(FormSerializer):
    create_organization_form = CreateOrganizationFormSerializer()


class CreateOrganizationApiView(APIView):
    @extend_schema(
        request=CreateOrganizationRequestSerializer,
        responses={
            201: OrganizationSerializer,
        },
        data=dict(),
        permissions=[
            (
                403,
                user_is_authenticated,
                "You must be authenticated to create an organization.",
            )
        ],
    )
    def post(self, request, request_data):
        try:
            organization = create_organization(request_data.create_organization_form)
        except OrganizationWithNameAlreadyExistsError:
            raise ValidationError(code="ORGANIZATION_NAME_ALREADY_EXISTS")

        update_checklist_item(
            user=request.user,
            checklist_item_name=ChecklistItemNames.ADD_ORGANIZATION,
            is_completed=True,
        )

        try:
            add_user_to_organization(
                organization, request.user, UserInOrganizationRoles.ADMIN
            )
        except UserAlreadyInOrganizationError:
            raise ValidationError(code="USER_ALREADY_IN_ORGANIZATION")

        return Response(
            OrganizationSerializer(organization).data, status=status.HTTP_201_CREATED
        )
